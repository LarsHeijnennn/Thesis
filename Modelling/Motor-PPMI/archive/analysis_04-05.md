# MDS-UPDRS Part III Longitudinal Motor Analysis

This repository contains [`analysis_04-05.ipynb`](Modelling/Motor-PPMI/in-progress/analysis_04-05.ipynb), a comprehensive Jupyter notebook for the quantitative and visual analysis of longitudinal motor assessment data from the MDS-UPDRS Part III scale in Parkinson’s Disease. The notebook is designed to support both exploratory and hypothesis-driven research on disease progression, medication effects, and data quality.

---

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Notebook Structure](#notebook-structure)
- [Key Analyses & Visualizations](#key-analyses--visualizations)
- [How to Run](#how-to-run)
- [Dependencies](#dependencies)
- [Interpretation & Next Steps](#interpretation--next-steps)
- [License](#license)

---

## Overview

The MDS-UPDRS Part III is a gold-standard clinical tool for quantifying motor symptoms in Parkinson’s Disease. This notebook provides:

- Data cleaning and preprocessing (handling special missing codes, date parsing, categorical conversion)
- Descriptive statistics and missingness analysis
- Longitudinal modeling of motor progression
- Stratified analysis by medication state (ON/OFF), visit, and treatment status
- Visualization of individual and group-level trajectories
- Quantification of progression rates and treatment effects

The workflow is suitable for both clinical researchers and data scientists interested in disease modeling, biomarker discovery, or clinical trial design.

---

## Dataset

- **Source:** `/Users/larsheijnen/Thesis/data/motor/MDS-UPDRS_Part_III_21Mar2025.csv`
- **Key columns:**
  - `PATNO`: Patient identifier
  - `EXAMDT`: Exam/visit date
  - `EVENT_ID`: Visit label (e.g., BL, V01, R01)
  - `PDSTATE`: Medication state at visit ("ON", "OFF", or missing)
  - `NP3TOT`: Total motor score (higher = worse)
  - `NHY`: Hoehn & Yahr stage (disease severity)
  - `PDTRTMNT`: Treatment status (1 = treated, 0 = untreated)
  - Additional NP3 subitems (e.g., `NP3SPCH`, `NP3FACXP`, `NP3RIGN`, `NP3GAIT`, `NP3BRADY`)

---

## Notebook Structure

### 1. Data Loading & Preprocessing

- Loads the raw CSV file.
- Replaces special missing value codes (e.g., 101.0) with `NaN`.
- Converts date columns to datetime and categorical columns to category type.
- Sorts data by patient and date, and assigns sequential visit numbers.

### 2. Data Exploration

- Summarizes missingness across all columns.
- Explores visit intervals and identifies paired ON/OFF assessments.
- Provides detailed column descriptions and interpretation.

### 3. Descriptive Statistics & Missingness

- Computes descriptive statistics for NP3TOT, NHY, and key subitems.
- Visualizes the distribution of NP3TOT and inter-item correlations.
- Stratifies NP3TOT by medication state (ON/OFF) and visit type.
- Visualizes missingness patterns with heatmaps.

### 4. Longitudinal & Treatment Analyses

- Plots individual patient trajectories and smoothed trends (LOWESS).
- Aggregates and visualizes mean NP3TOT by visit number.
- Calculates change from baseline for each patient.
- Fits linear mixed-effects models to estimate progression rates.
- Quantifies within-patient ON/OFF medication effects using paired visits.
- Compares treated vs. untreated patients over time.
- Computes annualized progression rates for NP3TOT and NHY.

### 5. Correlation & Advanced Visualization

- Computes and visualizes correlations between NP3TOT, NHY, and subitems.
- Generates spaghetti plots, mean/median trends, boxplots, and violin plots stratified by medication state and visit.

---

## Key Analyses & Visualizations

- **Descriptive statistics** for all key motor variables.
- **Missingness heatmaps** to identify problematic variables (notably NP3RIGN).
- **Individual and group-level progression plots** (raw and smoothed).
- **Linear mixed-effects modeling** for longitudinal progression.
- **Paired ON/OFF analysis** for robust within-patient medication effect estimation.
- **Treatment group comparisons** (treated vs. untreated).
- **Annualized progression rates** for both NP3TOT and NHY.
- **Correlation matrices** for composite and subitem relationships.
- **Advanced visualizations**: spaghetti plots, boxplots, violin plots.

---

## How to Run

1. **Clone this repository** and ensure you have access to the data file at the specified path.
2. **Install dependencies** (see below).
3. **Open** [`analysis_04-05.ipynb`](Modelling/Motor-PPMI/in-progress/analysis_04-05.ipynb) in Jupyter Notebook or VS Code.
4. **Run all cells** sequentially.

---

## Dependencies

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- scipy

Install with:

```sh
pip install pandas numpy matplotlib seaborn statsmodels scipy
```

---

## Interpretation & Next Steps

- **Progression:** The notebook demonstrates slow but significant progression in motor symptoms (~1 NP3TOT point/year on average), with substantial between-patient heterogeneity.
- **Medication effect:** ON/OFF paired analysis shows a robust, clinically meaningful improvement (~10 points) when ON medication.
- **Treatment group differences:** Treated patients have higher baseline severity and progress faster, but this may reflect confounding by indication.
- **Missingness:** NP3RIGN and some other subitems have notable missingness; appropriate handling (imputation, sensitivity analysis) is recommended.
- **Modeling:** The code provides a template for further mixed-effects modeling, predictive analytics, or causal inference.

---

## License

This analysis notebook is provided for research purposes. Please cite appropriately if used in publications.

---

**Contact:**  
For questions or suggestions, please contact the repository owner.
