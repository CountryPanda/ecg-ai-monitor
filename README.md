# Real-Time ECG Monitoring and AI-Based Abnormal Rhythm Detection with Emergency Alerts

A low-cost, real-time ECG monitoring system that captures ECG signals, processes them with digital signal processing (DSP), identifies potentially abnormal rhythm patterns using AI/ML, and generates an alert when a suspicious pattern is detected.

> **Disclaimer:** This project is an educational early-warning prototype. It is **not** a medical diagnostic device and must not be used for clinical decisions.

**Team:** Six members

---

## 1. Problem Statement

Heart rhythm abnormalities can occur unexpectedly, and a person is not always under continuous medical observation. This project proposes an affordable, real-time ECG monitoring system that continuously analyses the heart signal and raises an alert when an abnormal pattern is suspected.

## 2. Objectives

- Acquire a clean ECG signal in real time using low-cost hardware
- Filter noise and baseline drift, detect R-peaks and compute heart rate
- Train an AI/ML model to classify normal vs. abnormal rhythms using public ECG datasets
- Run the trained model on live ECG data in real time
- Trigger local alerts, with confirmation logic to reduce false alarms
- Document the design, test results, limitations and future improvements

## 3. System Architecture

The system is split across two Raspberry Pi 3 B+ units:

| Unit | Responsibility |
|------|----------------|
| **Unit 1** | ECG signal acquisition, preprocessing and filtering |
| **Unit 2** | Runs the trained AI model for inference on the processed signal |

**System flow**

```
ECG Electrodes → AD8232 Front-End → ADC → Unit 1 (Acquisition + Filtering)
   → ECG Segmentation → Unit 2 (AI Model) → Prediction → Alert
```

## 4. Hardware Components

**Compute:** 2 × Raspberry Pi 3 B+, 2 × 16 GB microSD cards, 2 × Pi power adapters

**Sensing and conversion:** AD8232 ECG sensor, MCP3008, ECG electrodes and cable

**Display and logging:** Raspberry Pi Display, RTC module

**Alerts (optional demo feature):** 5V relay module, electronic buzzer

**Prototyping:** Breadboard, jumper wires, resistors, capacitors, transistors, ICs

**Bench tools:** Bench power supply, 70 MHz digital storage oscilloscope, 2-channel arbitrary function generator, soldering/desoldering station, digital multimeter, tweezers, wire stripper, screwdriver set

## 5. Software and Tools

- Python
- NumPy and Pandas: data handling
- SciPy: ECG filtering and signal processing
- Matplotlib: ECG visualization
- scikit-learn and/or TensorFlow: AI/ML
- Public ECG datasets for training and evaluation

## 6. Methodology

1. **Acquisition:** capture the analog ECG and digitize it with an ADC.
2. **Preprocessing:** remove baseline drift and high-frequency noise; detect R-peaks and RR intervals; compute heart rate.
3. **Segmentation:** split the signal into fixed segments suitable for the model.
4. **Model development:** select and label a public dataset, split into training/validation/test sets, train and compare candidate models, and evaluate using accuracy, precision, recall and a confusion matrix.
5. **Real-time inference:** apply the same preprocessing pipeline used in training to live data and run the model on incoming segments.
6. **Alerting:** trigger buzzer/relay alerts, using confirmation logic so isolated noisy segments do not cause false alarms.
7. **Monitoring and logging:** display ECG, heart rate, prediction and system status, and log data for later analysis.

## 7. Project Phases

| Weeks | Phase | Expected Output |
|-------|-------|-----------------|
| 1–4 | Foundation, hardware and ECG acquisition | Functional ECG acquisition and live waveform |
| 5–8 | Signal processing and AI dataset preparation | Stable preprocessing pipeline and AI-ready dataset |
| 9–12 | AI model development and real-time integration | Working real-time ECG monitoring with AI prediction |
| 13–16 | Alerts, full integration, testing and finalization | Complete, tested, presentation-ready prototype |

## 8. Milestones

- **End of Week 4:** Live ECG signal captured and displayed
- **End of Week 8:** Filtering, heart-rate detection and AI-ready dataset complete
- **End of Week 12:** AI model selected; real-time ECG-to-AI prediction demonstrated
- **End of Week 16:** Alerts, full integration, testing, documentation and final presentation complete

## 9. Team Roles

| Member | Focus |
|--------|-------|
| Member 1 | Hardware setup and ECG acquisition |
| Member 2 | Signal filtering and processing |
| Member 3 | Dataset preparation and AI/ML model |
| Member 4 | Real-time software integration |
| Member 5 | Alert system |
| Member 6 | Documentation, testing and coordination |

## 10. Expected Outcome

By November 2026, a working prototype that acquires ECG in real time, processes and visualizes the signal, calculates heart rate, uses an AI/ML model to identify potentially abnormal rhythms, and generates local alerts, along with documented test results, limitations and future improvements.

## 11. Limitations

- Not clinically validated; for educational use only
- Signal quality depends on electrode placement and contact
- Model performance depends on the training dataset and the rhythm classes chosen

## 12. Future Improvements

- SMS/GSM emergency alerts
- Compact enclosure or wearable form factor
- Larger, more diverse datasets and additional rhythm classes
- Wireless data transfer and mobile app integration
