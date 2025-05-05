# Analysis of MDS-UPDRS Part III Motor Scores

This repository contains a Jupyter Notebook (`analysis_04-05.ipynb`) for analyzing motor examination data from the MDS-UPDRS Part III assessment. The notebook walks through data loading, preprocessing, statistical analysis, and visualization steps to explore Parkinson’s Disease motor scores over multiple clinical visits.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Data](#data)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Notebook Structure](#notebook-structure)
7. [Results Summary](#results-summary)
8. [License](#license)

## Project Overview

This analysis aims to:

- Calculate time intervals between patient visits.
- Identify and compare paired ON/OFF state visits.
- Explore trends in total motor scores (NP3TOT) across visits.
- Examine correlations between NP3TOT, Hoehn & Yahr stage (NHY), and key motor items.
- Visualize score distributions and trends.

## Prerequisites

- Python 3.8 or higher
- Jupyter Notebook
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - statsmodels
  - scipy

Install dependencies via pip:
```bash
pip install pandas numpy matplotlib seaborn statsmodels scipy
```

## Data

Place the MDS-UPDRS Part III CSV file in your local directory and update the `DATA_DIR` path at the top of the notebook:
```python
DATA_DIR = '/path/to/MDS-UPDRS_Part_III_21Mar2025.csv'
```

The CSV should include at least the following columns:

- `PATNO`: Patient identifier
- `EVENT_ID`: Visit identifier
- `PDSTATE`: Medication state (ON/OFF)
- `NP3TOT`: Total motor score
- `NHY`: Hoehn & Yahr stage
- Date or timestamp columns for visit dates

## Installation

1. Clone this repository:
   ```bash
git clone <repository_url>
cd <repository_folder>
```
2. Install dependencies (see Prerequisites).

## Usage

1. Launch Jupyter Notebook:
   ```bash
jupyter notebook analysis_04-05.ipynb
```
2. Execute cells sequentially to reproduce the analysis and visualizations.

## Notebook Structure

The notebook is organized into the following steps:

- **Step 1**: Load data and inspect.
- **Step 2**: Compute visit-to-visit time differences.
- **Step 3**: Identify paired ON/OFF visits and summarize counts.
- **Step 4**: Calculate and plot summary statistics by PD state.
- **Step 5**: Analyze correlations between NP3TOT, NHY, and key motor items.
- **Step 6**: Lowess smoothing of NP3TOT vs. visit number.
- **Step 7**: Visualize distributions (boxplots and violin plots) of NP3TOT by visit and PD state.

Each section includes descriptions of column meanings, interpretations, and key findings.

## Results Summary

- Visit intervals vary widely between patients; median interval is X days.
- Y paired ON/OFF visit records identified across Z patients.
- Moderate correlation (r ≈ 0.6) between NP3TOT and NHY stage.
- Smoothed trend shows gradual increase in motor scores over successive visits.
- Violin plots reveal greater score variability in OFF state.

*(Adjust summary statistics with actual results from the notebook.)*

## License

This project is released under the MIT License. Feel free to use and adapt for your research.
