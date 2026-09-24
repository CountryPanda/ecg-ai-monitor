# ECG AI/ML Model

## Overview

This folder contains the Artificial Intelligence / Machine Learning component of the ECG monitoring project.

The objective is to classify individual ECG beats into three classes:

- Normal
- PVC (Premature Ventricular Contraction)
- Other Abnormal

The model is developed using Python and ECG data from the MIT-BIH Arrhythmia Database. The final model is intended to be integrated with the Raspberry Pi-based ECG acquisition system.

## Project Pipeline

```text
MIT-BIH ECG Dataset
        ↓
ECG Signal Processing
        ↓
Beat Detection / Annotation
        ↓
Feature Extraction
        ↓
Feature Engineering
        ↓
Machine Learning Model
        ↓
Record-wise Cross Validation
        ↓
Performance Evaluation
        ↓
Future Raspberry Pi Integration
```

## Dataset

The model uses records from the MIT-BIH Arrhythmia Database.

| Class | Description |
|---|---|
| Normal | Normal heartbeat |
| PVC | Premature Ventricular Contraction |
| Other Abnormal | Other abnormal heartbeat patterns |

After preprocessing and warm-up removal:

| Class | Number of beats |
|---|---:|
| Normal | 27,104 |
| PVC | 3,661 |
| Other Abnormal | 2,634 |
| **Total** | **33,399** |

## Features

### Original Features

- `rr_prev` – Previous RR interval
- `rr_next` – Next RR interval
- `rr_ratio` – RR interval ratio
- `amplitude` – Beat amplitude
- `std` – Signal standard deviation
- `mean` – Signal mean
- `qrs_width` – QRS width
- `slope` – Signal slope

### Causal Relative Features

- `amplitude_rel`
- `std_rel`
- `qrs_width_rel`
- `slope_rel`
- `rr_norm_prev_causal`

The causal features use previous beats to establish a rolling baseline. A 50-beat rolling window was used, followed by removal of the initial warm-up period.

## Machine Learning Model

A Random Forest Classifier is used for heartbeat classification.

```python
RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)
```

## Validation

The model is evaluated using **5-fold Stratified Group K-Fold Cross Validation**.

The ECG record number is used as the group so that beats from the same record are not simultaneously used for training and testing in the same fold.

## Current Results

| Feature Set | Accuracy | Macro F1 | Normal Recall | PVC Recall | Other Abnormal Recall |
|---|---:|---:|---:|---:|---:|
| orig9 | 82.26% | 0.5484 | 90.66% | 74.23% | 6.95% |
| orig8 | 83.14% | 0.5614 | 90.93% | 80.40% | 6.85% |
| causal13 | **84.84%** | **0.5801** | **92.84%** | **82.38%** | 5.91% |

The causal feature set improves overall accuracy and PVC/Normal recall, but Other Abnormal recall remains low.

## Difficult Records

Record-wise analysis identified difficult ECG records, particularly:

- Record 208
- Record 209
- Record 232

Many Other Abnormal beats in these records are classified as Normal. This remains an important area of investigation.

## Leakage Prevention

During development, record-level information leakage was investigated.

Features using future beats or full-record statistics can produce overly optimistic validation results. Therefore, causal relative features were created using only previous beats.

The causal baseline is calculated from previous observations using a rolling median.

## Current Status

**Model development and validation are in progress.**

The current causal model improves overall record-wise performance, but further investigation is required before selecting the final model for live deployment.

## Future Work

1. Investigate difficult records.
2. Improve Other Abnormal detection.
3. Evaluate additional ECG morphology and rhythm features.
4. Determine whether the three-class model is sufficiently reliable or whether a binary Normal/Abnormal model is more appropriate.
5. Finalize the validated feature set and model.
6. Export the final model using `joblib`.
7. Integrate the model with live ECG data from the AD8232 sensor and Raspberry Pi.
8. Connect the ML output to the software interface and alert system.

## Hardware Integration

```text
AD8232 ECG Sensor
        ↓
MCP3008 ADC
        ↓
Raspberry Pi 3B+
        ↓
ECG Signal Processing
        ↓
Feature Extraction
        ↓
ML Model
        ↓
Heartbeat Classification
        ↓
Software Display / Alerts
```

## Technologies Used

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- MIT-BIH Arrhythmia Database
- Random Forest
