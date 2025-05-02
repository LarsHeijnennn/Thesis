# MDS-UPDRS Part III Quantitative Analysis

## Overview

This Jupyter Notebook performs a quantitative analysis of longitudinal data from the Movement Disorder Society - Unified Parkinson's Disease Rating Scale (MDS-UPDRS) Part III (Motor Examination). The goal is to explore patterns of motor symptom progression in Parkinson's Disease (PD) patients over time, examine the effects of medication states (ON/OFF), and quantify relationships between different motor scores. The analysis includes data cleaning, descriptive statistics, visualizations, and statistical modeling suitable for longitudinal clinical data.

## Dataset Description

The analysis uses the `MDS-UPDRS_Part_III_21Mar2025.csv` dataset (or a similarly named full version).

- **Content:** Longitudinal MDS-UPDRS Part III motor scores for PD patients across multiple visits.
- **Key Identifiers:**
  - `PATNO`: Unique patient identifier.
  - `EVENT_ID`: Visit identifier (e.g., `BL`, `V01`, `V04`).
  - `REC_ID`: Unique record identifier for each assessment row.
- **Primary Outcome:**
  - `NP3TOT`: Total MDS-UPDRS Part III score (higher score indicates worse motor function).
  - Individual `NP3...` item scores are also present.
- **Key Covariates/Stratifiers:**
  - `EXAMDT` / `INFODT`: Date of examination/information. Crucial for temporal analysis.
  - `PDSTATE`: Patient's medication state ('ON' or 'OFF') during the assessment.
  - `NHY`: Hoehn and Yahr stage (clinical severity).
  - `PDTRTMNT`: Flag indicating if the patient received PD treatment.
- **Special Values:** Value `101.0` in score columns is treated as missing (`NaN`).
- **Format:** CSV file.

## Setup / Requirements

This notebook uses the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `scipy`

Install them via pip:

```bash
pip install pandas numpy matplotlib seaborn statsmodels scipy
```

## Analysis Steps

### Step 1: Load Data

- **Code Cell:** 2
- **Action:** Load CSV into a DataFrame named `data`.

### Step 2: Data Cleaning and Preparation

- **Code Cell:** 4
- **Actions:**
  - Replace `101.0` in `NP3` columns with `NaN`.
  - Convert date columns using `pd.to_datetime`.
  - Convert categorical columns (`EVENT_ID`, `PAG_NAME`, `PDSTATE`) to `category` dtype.

### Step 3: Longitudinal Structuring & Exploratory Checks

- **Code Cells:** 6, 7, 8
- **Actions:**
  - Sort by `PATNO` and `EXAMDT`.
  - Create `VISIT_NUM` with `groupby('PATNO').cumcount()`.
  - Check visit intervals and presence of paired ON/OFF assessments.

### Step 4: Descriptive Statistics

- **Code Cells:** 10, 11, 13
- **Actions:**
  - Compute `.describe()` stats for key items overall.
  - Stratify by `PDSTATE` and `EVENT_ID`.

### Step 5: Visualizations

- **Code Cells:** 14, 16, 17
- **Actions:**
  - Heatmap of missingness using `seaborn.heatmap`.
  - Faceted patient trajectories for top 5 patients.
  - LOWESS-smoothed combined plot of `NP3TOT` over time.

### Step 6: Quantitative Longitudinal Analysis

- **Code Cells:** 20–24
- **Actions:**
  - Calculate change from baseline.
  - Fit Linear Mixed Model (LMM) for `NP3TOT` ~ `DAYS_SINCE_BL`.
  - ON vs. OFF within-visit comparison.
  - Compare treated vs. untreated progression.
  - Compute annualized change rates for `NP3TOT` and `NHY`.

### Step 7: Correlation Analysis

- **Code Cell:** 25
- **Actions:**
  - Pearson correlation between `NP3TOT` and `NHY`.
  - Pairwise correlation matrix for motor scores.

## Key Findings / Outputs

- Descriptive statistics tables (overall, by `PDSTATE`, by `EVENT_ID`).
- Heatmap of data missingness.
- Raw and smoothed individual trajectories.
- Linear Mixed Model summary.
- ON/OFF within-patient difference summary.
- Plot: treated vs. untreated average progression.
- Annualized rate summaries.
- Pearson `r` and correlation matrix.

## Next Steps / Future Work

- Address pandas warnings (e.g., `observed=` in `groupby`, datetime format).
- Investigate `101.0` values with data dictionary.
- Explore more complex models (e.g., random slopes, non-linear).
- Subgroup analyses (e.g., by treatment or baseline severity).
- Incorporate more covariates (age, sex, duration).
- Apply missing data techniques if needed.
- Dive deeper into individual `NP3...` items.
- Compare analysis using `EXAMDT` vs. `INFODT`.

## How to Use

1. **Install Libraries:** Ensure all required libraries are installed.
2. **Load Data:** Place `MDS-UPDRS_Part_III_21Mar2025.csv` in the appropriate path.
3. **Run Notebook:** Open and run `test.ipynb` sequentially.
4. **Review Outputs:** Use the tables and plots to interpret analysis results.