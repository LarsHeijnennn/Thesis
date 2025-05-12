# Predicting Motor Symptom Progression in Parkinson’s Disease Using PPMI Data

## Overview

This repository contains a Jupyter Notebook (`motor_ppmi_time_lag_3.ipynb`) that implements a machine learning pipeline to predict the progression of motor symptoms in Parkinson’s disease (PD) patients. The analysis leverages longitudinal clinical data from the Parkinson’s Progression Markers Initiative (PPMI) database, focusing on forecasting the total score of the Movement Disorder Society Unified Parkinson’s Disease Rating Scale Part III (MDS-UPDRS Part III) at a patient’s next clinical visit.

---

## Methodology

### 1. Data Acquisition and Preparation
- **Data Source**: `MDS-UPDRS_Part_III_21Mar2025.csv`
- **Feature Selection**: Includes patient ID (`PATNO`), visit ID (`EVENT_ID`), date (`INFODT`), individual item scores, and total score (`NP3TOT`)
- **Cleaning**: Removes missing `NP3TOT` values and invalid dates
- **Sorting**: Data is sorted chronologically for each patient

### 2. Feature Engineering
- **Temporal Features**: `days_since_baseline`
- **Target Variable**: `NP3TOT_next_visit`
- **Lag Features**: `NP3TOT_lag1`, `lag2`, `lag3`
- **Difference Features**: `NP3TOT_diff1`, `diff2`, `diff3`
- **Time Interval Features**: `days_since_prev1`, `prev2`, `prev3`
- **Filtering**: Rows with NaNs after feature creation are removed

### 3. Data Splitting (Group-Based)
- **Features (X)**: Includes NP3 items, temporal, lag, difference, and interval features
- **Target (y)**: `NP3TOT_next_visit`
- **Group Split**: `GroupShuffleSplit` ensures no patient overlap between train/test sets

### 4. Data Scaling
- **Standardization**: `StandardScaler` fit on training data, applied to both train/test sets

### 5. Model Selection and Training
- **Models Evaluated**:
  - Linear Regression
  - Support Vector Regressor (SVR)
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - XGBoost Regressor
  - K-Neighbors Regressor
  - AdaBoost Regressor
  - MLP Regressor

### 6. Evaluation on Test Set
- **Metrics**: MAE, RMSE, R²
- **Visualization**: Scatter plots of actual vs. predicted scores
- **Results Saved**: `model_results_progression_test_lag3.csv`

### 7. Cross-Validation (Group-Based)
- **Strategy**: 5-fold `GroupKFold`
- **Out-of-Fold Predictions**: via `cross_val_predict`
- **Metrics**: MAE, RMSE, R²
- **Results Saved**: `model_results_progression_test__cv_lag3.csv`

---

## Results

### Model Performance on Held-Out Test Set

**Key Findings**:
- **Random Forest** and **Gradient Boosting Regressors** had the best MAE/RMSE.
- **XGBoost** was robust and competitive.
- **Linear Regression** and **SVR** underperformed.
- **MLP** and **KNeighbors** were moderate performers.
- **R²** values were modest — indicating partial explanation of motor progression variance.

**Prediction Visualization**:
- Scatter plots show accurate tracking at lower scores; higher score predictions had more variance.

### Cross-Validation Results

- Ensemble models consistently outperformed others.
- Metrics were consistent across cross-validation and test sets.
- R² values confirmed predictive limits due to PD complexity.

---

## Summary Table

Performance metrics are saved as CSV files:

- Test Set: `model_results_progression_test_lag3.csv`
- Cross-Validation: `model_results_progression_test__cv_lag3.csv`

| Model                  | MAE  | RMSE | R²   |
|------------------------|------|------|------|
| RandomForest Regressor| ...  | ...  | ...  |
| GradientBoosting       | ...  | ...  | ...  |
| XGBoost                | ...  | ...  | ...  |
| Linear Regression      | ...  | ...  | ...  |
| SVR                    | ...  | ...  | ...  |
| KNeighbors             | ...  | ...  | ...  |
| AdaBoost               | ...  | ...  | ...  |
| MLP Regressor          | ...  | ...  | ...  |

_(Fill in the actual values from notebook outputs)_

---

## Interpretation

Tree-based ensemble models are best suited for short-term motor progression prediction using longitudinal clinical data and engineered temporal features. However, the modest R² values indicate that more sophisticated features or modeling strategies may be necessary for further improvements.

This work provides a reproducible pipeline for patient-level progression modeling in longitudinal clinical studies.

---

## Usage

1. Place the PPMI MDS-UPDRS Part III CSV file in the `data/` directory.
2. Run the `motor_ppmi_time_lag_3.ipynb` notebook in a Jupyter environment.
3. Review output plots and CSVs for performance metrics and comparisons.

---

## Citation

If you use this code or methodology, please cite the PPMI study and this repository appropriately.

---

## Contact

For questions or collaboration, please contact the repository maintainer.
