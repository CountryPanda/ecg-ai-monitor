# Hardware Setup & ECG Acquisition (Unit 1)

## Overview
Unit 1 acquires raw ECG signal using an AD8232 sensor and an MCP3008 ADC, read by a Raspberry Pi 3 B+ over SPI. This covers Phase 1 (Weeks 1-4) of the project: hardware assembly, wiring, and first successful live signal capture.

## Hardware
- Raspberry Pi 3 B+ (`ecg-unit1`)
- AD8232 ECG sensor
- MCP3008 10-bit ADC
- Breadboard + jumper wires
- 3-lead ECG cable + disposable electrode pads

## Wiring

| From | To |
|---|---|
| AD8232 OUTPUT | MCP3008 CH0 (Pin 1) |
| AD8232 3.3V | Shared 3.3V rail |
| AD8232 GND | Shared GND rail |
| AD8232 LO+ | Pi GPIO17 |
| AD8232 LO- | Pi GPIO27 |
| MCP3008 VDD (Pin 16) | 3.3V rail |
| MCP3008 VREF (Pin 15) | 3.3V rail |
| MCP3008 AGND (Pin 14) | GND rail |
| MCP3008 DGND (Pin 9) | GND rail |
| MCP3008 CLK (Pin 13) | Pi GPIO11 / SCLK (physical 23) |
| MCP3008 DOUT (Pin 12) | Pi GPIO9 / MISO (physical 21) |
| MCP3008 DIN (Pin 11) | Pi GPIO10 / MOSI (physical 19) |
| MCP3008 CS/SHDN (Pin 10) | Pi GPIO8 / CE0 (physical 24) |

## Setup
1. Flashed Raspberry Pi OS (64-bit) via Raspberry Pi Imager, hostname `ecg-unit1`, SSH enabled
2. Enabled SPI: `sudo raspi-config` → Interface Options → SPI
3. Verified: `ls /dev/spi*` → `/dev/spidev0.0`, `/dev/spidev0.1`
4. Installed dependencies:
   ```
   pip3 install spidev --break-system-packages
   ```

## Scripts
- [`ecgadcvalues.py`](./ecgadcvalues.py) – reads MCP3008 channel 0 over SPI, checks AD8232 leads-off status (LO+/LO-) via `RPi.GPIO` before each read, prints raw 10-bit ADC values (0-1023).
  ```
  python3 ecgadcvalues.py
  ```
- [`ecg_plot.py`](./ecg_plot.py) – live matplotlib plot of the raw ADC signal (rolling 200-sample window). Requires a display (run via HDMI-connected desktop session).
  ```
  python3 ecg_plot.py
  ```

## Verification
- SPI chain confirmed functional via direct short tests (3.3V→CH0 reads ~1023, GND→CH0 reads ~0)
- Live acquisition confirmed: real fluctuating values captured (e.g. 138, 100, 314, 335, 723)
- Leads-off detection correctly triggers on poor/lost electrode contact
- Live raw waveform successfully rendered via `ecg_plot.py`

## Known issues / notes
- Signal is raw and unfiltered — visible noise/motion artifacts present; filtering and R-peak detection are out of scope for M1
- Power: use a stable 5V/2.5A+ source (Pi official adapter recommended); a Xiaomi MDY-17-EC (5V/3A) charger was used as a working substitute during dev — cheap/phone fast-chargers without proper handshake support caused undervoltage/HDMI flicker
- AD8232 boards may include a spare unused pad near GND (duplicate electrode connector, alternate to the 3.5mm jack) — safe to leave unconnected

## Status
  Phase 1 milestone met: "Live ECG signal successfully captured and displayed"
**Next:** hand off to M2/M4 for filtering, R-peak detection, and heart-rate calculation.
