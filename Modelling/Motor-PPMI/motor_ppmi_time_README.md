# Predicting Short-Term Parkinson's Motor Symptom Progression (MDS-UPDRS Part III)

## Overview

This Jupyter Notebook focuses on predicting the short-term progression of motor symptoms in Parkinson's disease (PD) patients using data from the Parkinson's Progression Markers Initiative (PPMI). Specifically, it aims to build and evaluate various machine learning regression models to predict the **MDS-UPDRS Part III total score (NP3TOT)** of a patient's *next* clinical visit, based *only* on motor assessment data collected during their *current* visit and some engineered time-related features.

The analysis employs a unimodal approach, relying solely on the `MDS-UPDRS_Part_III_21Mar2025.csv` dataset.

## Goal

The primary objectives of this notebook are:

1.  **Establish Baseline Performance:** Determine how well standard regression models can predict the next NP3TOT score using only current motor assessment scores and basic temporal information (time since baseline, previous score).
2.  **Compare Regression Models:** Evaluate and compare the performance of several common regression algorithms for this specific time-series prediction task on clinical data.
3.  **Apply Appropriate Validation:** Utilize validation techniques suitable for longitudinal patient data (Group-based splitting and cross-validation) to obtain reliable estimates of model generalization performance and avoid data leakage between patient records.

## Methodology

The notebook follows a standard machine learning pipeline tailored for longitudinal clinical data:

1.  **Data Loading and Selection:** Reads the motor assessment data and selects relevant features.
2.  **Data Cleaning:** Handles missing values and ensures correct data types, particularly for dates.
3.  **Chronological Sorting:** Sorts data per patient by visit date, essential for time-based analysis.
4.  **Feature Engineering:** Creates the prediction target and incorporates temporal dynamics.
5.  **Data Splitting:** Separates data into training and testing sets while keeping all records for a single patient within the same set (`GroupShuffleSplit`).
6.  **Preprocessing:** Scales numerical features using `StandardScaler`, fitting *only* on the training data.
7.  **Model Training:** Trains various regression models on the scaled training data.
8.  **Evaluation:**
    *   Evaluates models on the held-out test set.
    *   Performs group-aware cross-validation (`GroupKFold`) on the training set to assess robustness.
9.  **Results Reporting:** Saves performance metrics and generates visualizations.

## Data

*   **Input File:** `/Users/larsheijnen/Thesis/data/MDS-UPDRS_Part_III_21Mar2025.csv`
*   **Source:** Parkinson's Progression Markers Initiative (PPMI)
*   **Key Identifiers:** `PATNO` (Patient ID), `EVENT_ID` (Visit ID), `INFODT` (Visit Date)
*   **Features Used (X):**
    *   Individual MDS-UPDRS Part III item scores from the *current* visit (e.g., `NP3SPCH`, `NP3FACXP`, `NP3RIGN`, `NP3RIGRU`, ..., `NP3RTCON`). Note: `NP3TOT` itself is *not* used as a direct feature for predicting the *next* score, though it's used to create lag features.
    *   Engineered time features: `days_since_baseline`, `NP3TOT_lag1`, `NP3TOT_diff1`.
*   **Target Variable (y):** `NP3TOT_next_visit` (The MDS-UPDRS Part III total score from the patient's subsequent visit).

## Feature Engineering

To capture temporal dynamics and define the prediction task, the following features are engineered for each visit record (where applicable):

1.  **`days_since_baseline`**: Calculated as the number of days elapsed between the current visit (`INFODT`) and the patient's first recorded visit in the dataset. Provides a measure of time within the study for each patient.
2.  **`NP3TOT_next_visit` (Target):** The `NP3TOT` score from the *next chronological visit* for the same patient. Created using `groupby('PATNO')['NP3TOT'].shift(-1)`. Records corresponding to a patient's last visit will have NaN for this target and are subsequently dropped.
3.  **`NP3TOT_lag1`**: The `NP3TOT` score from the *previous chronological visit* for the same patient. Created using `groupby('PATNO')['NP3TOT'].shift(1)`. Incorporates the immediate past score as a predictor. Records corresponding to a patient's first visit will have NaN for this feature and are subsequently dropped.
4.  **`NP3TOT_diff1`**: The difference between the *current* `NP3TOT` and the *previous* `NP3TOT` (`NP3TOT_lag1`). Created using `groupby('PATNO')['NP3TOT'].diff(1)`. Captures the recent change in score. Records corresponding to a patient's first visit will have NaN for this feature and are subsequently dropped.

## Preprocessing

*   **Scaling:** `StandardScaler` is used to standardize features by removing the mean and scaling to unit variance. **Crucially, the scaler is `fit` only on the training data (`X_train`) and then used to `transform` both the training (`X_train`) and test (`X_test`) sets.** This prevents information leakage from the test set into the training process.

## Validation Strategy

Handling longitudinal data requires careful validation to avoid overly optimistic results:

1.  **Train-Test Split:** `GroupShuffleSplit` is used to create a single train/test split (80%/20%). The `groups` parameter is set to `PATNO`, ensuring that *all* visit records for a given patient reside entirely within either the training set or the test set. This simulates predicting progression for unseen patients.
2.  **Cross-Validation:** `GroupKFold` (with 5 folds) is used for cross-validation *within the training set*. Again, the `groups` parameter ensures patient data integrity within folds. This provides a more robust estimate of model performance and variability without touching the final test set.

## Models Evaluated

The following regression models are trained and compared:

*   Linear Regression (`sklearn.linear_model.LinearRegression`)
*   Support Vector Regressor (`sklearn.svm.SVR`)
*   Random Forest Regressor (`sklearn.ensemble.RandomForestRegressor`)
*   Gradient Boosting Regressor (`sklearn.ensemble.GradientBoostingRegressor`)
*   XGBoost Regressor (`xgboost.XGBRegressor`)
*   K-Neighbors Regressor (`sklearn.neighbors.KNeighborsRegressor`)
*   AdaBoost Regressor (`sklearn.ensemble.AdaBoostRegressor`)
*   Multi-layer Perceptron Regressor (`sklearn.neural_network.MLPRegressor`)

## Evaluation Metrics

Model performance is assessed using standard regression metrics:

*   **Mean Absolute Error (MAE):** Average absolute difference between predicted and actual values. Interpretable in the original units of NP3TOT.
*   **Root Mean Squared Error (RMSE):** Square root of the average squared difference. Penalizes larger errors more heavily than MAE. Also in the original units.
*   **R-squared (R²):** Coefficient of determination. Represents the proportion of the variance in the target variable that is predictable from the features. Ranges from -∞ to 1 (higher is better, 1 is perfect prediction, 0 means the model is no better than predicting the mean).

## Workflow Steps

1.  **Load Data:** Read the CSV file.
2.  **Initial Feature Selection:** Keep relevant motor score columns and identifiers.
3.  **Clean Data:** Drop rows with missing `NP3TOT`, convert `INFODT` to datetime and drop conversion errors.
4.  **Sort Data:** Order by `PATNO` and `INFODT`.
5.  **Engineer Features:** Calculate `days_since_baseline`, `NP3TOT_next_visit`, `NP3TOT_lag1`, `NP3TOT_diff1`.
6.  **Prepare Final Dataset:** Drop rows with NaN values resulting from the `shift` and `diff` operations (first/last visits per patient).
7.  **Define X, y, groups:** Isolate features, target, and patient identifiers.
8.  **Split Data:** Perform the 80/20 group-aware train/test split.
9.  **Scale Features:** Fit `StandardScaler` on `X_train` and transform `X_train` and `X_test`.
10. **Train & Evaluate on Test Set:** Train each model on scaled training data, predict on scaled test data, calculate metrics, visualize predictions, and save results to `model_results_progression_test.csv`.
11. **Cross-Validate on Training Set:** Perform 5-fold `GroupKFold` cross-validation using `cross_val_predict` on the scaled training data, calculate metrics, visualize predictions, and save results to `model_results_progression_cv.csv`.

## Results

The notebook outputs:

1.  **Console Prints:** Performance metrics (MAE, RMSE, R²) for each model on both the test set and via cross-validation on the training set.
2.  **Scatter Plots:** Visualizations of actual vs. predicted `NP3TOT_next_visit` for each model, generated for both the test set evaluation and the cross-validation results.
3.  **CSV Files:**
    *   `/Users/larsheijnen/Thesis/Motor-PPMI/results_motor/model_results_progression_test.csv`: Contains MAE, RMSE, and R-squared for each model evaluated on the single hold-out test set.
    *   `/Users/larsheijnen/Thesis/Motor-PPMI/results_motor/model_results_progression_cv.csv`: Contains MAE, RMSE, and R-squared for each model based on the 5-fold group cross-validation performed on the training set.

## How to Run

1.  **Environment:** Ensure you have a Python environment with the necessary dependencies installed (see below).
2.  **Data:** Place the `MDS-UPDRS_Part_III_21Mar2025.csv` file in the directory specified in the code: `/Users/larsheijnen/Thesis/data/`.
3.  **Output Directory:** Ensure the output directory exists or create it: `/Users/larsheijnen/Thesis/Motor-PPMI/results_motor/`. Alternatively, modify the output paths within the notebook code.
4.  **Execution:** Run the cells of the Jupyter Notebook sequentially from top to bottom.

## Dependencies

*   pandas
*   numpy
*   matplotlib
*   seaborn
*   scipy
*   scikit-learn (`sklearn`)
*   xgboost
*   csv (standard library)

You can typically install these using pip:
`pip install pandas numpy matplotlib seaborn scipy scikit-learn xgboost`

## Potential Improvements / Future Work

*   **Hyperparameter Tuning:** Optimize hyperparameters for each model (e.g., using `GridSearchCV` or `RandomizedSearchCV` with group-aware CV).
*   **Feature Engineering:** Explore more sophisticated time-based features (e.g., rolling averages, rate of change over longer periods, time between visits).
*   **Advanced Models:** Investigate models designed for sequential data (e.g., Recurrent Neural Networks - LSTMs, GRUs), although this would require restructuring the data input.
*   **Multimodal Analysis:** Incorporate data from other PPMI assessments (e.g., non-motor symptoms, biospecimens, imaging) to potentially improve predictions.
*   **Error Analysis:** Investigate where models perform poorly (e.g., specific patient groups, prediction horizons).

## Disclaimer

This notebook uses data obtained from the Parkinson's Progression Markers Initiative (PPMI) database (www.ppmi-info.org/data). For up-to-date information on the study, visit www.ppmi-info.org. The analysis presented here is for research and illustrative purposes. Clinical decisions should not be made based solely on the predictions from these models.