import spidev
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from collections import deque

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

AD8232_LO_POS_PIN = 17
AD8232_LO_NEG_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(AD8232_LO_POS_PIN, GPIO.IN)
GPIO.setup(AD8232_LO_NEG_PIN, GPIO.IN)


def read_adc(channel):
    adc_command = [0x01, (0x80 | channel) << 4, 0x00]
    adc_data = spi.xfer2(adc_command)
    adc_value = ((adc_data[1] & 0x03) << 8) + adc_data[2]
    return adc_value


# Rolling window of the last 200 samples
window_size = 200
data = deque([512] * window_size, maxlen=window_size)

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(data)
ax.set_ylim(0, 1023)
ax.set_title("Live ECG signal (raw ADC)")
ax.set_xlabel("Samples")
ax.set_ylabel("ADC value")

try:
    while True:
        lo_pos_status = GPIO.input(AD8232_LO_POS_PIN)
        lo_neg_status = GPIO.input(AD8232_LO_NEG_PIN)

        if lo_pos_status == 1 or lo_neg_status == 1:
            pass  # keep last value, skip plotting a bad point
        else:
            adc_value = read_adc(0)
            data.append(adc_value)

        line.set_ydata(data)
        line.set_xdata(range(len(data)))
        ax.relim()
        ax.autoscale_view(scalex=False)
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

spi.close()
GPIO.cleanup()
