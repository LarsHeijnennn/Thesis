# MDS-UPDRS Part III Analysis & Prediction

This repository contains two Jupyter notebooks for the analysis and modeling of MDS-UPDRS (Movement Disorder Society-Unified Parkinson's Disease Rating Scale) Part III data. The primary goal is to explore the data and build machine learning models to predict the progression of Parkinson's disease motor symptoms, focusing on the NP3TOT (Total score of MDS-UPDRS Part III).

---

## Table of Contents

- [Project Structure](#project-structure)
- [Notebooks Overview](#notebooks-overview)
  - [1. EDA_and_timeseries.ipynb](#1-eda_and_timeseriesipynb)
  - [2. ML.ipynb](#2-mlipynb)
- [Data Source](#data-source)
- [Dependencies](#dependencies)
- [Setup & Usage](#setup--usage)
- [Reproducibility](#reproducibility)
- [Notes](#notes)

---

## Project Structure
Final/
├── EDA_and_timeseries.ipynb # Exploratory Data Analysis & Time Series Exploration
├── ML.ipynb # Machine Learning Modeling & Evaluation
├── MDS-UPDRS_Part_III_21Mar2025.csv # Main dataset (not included in repo due to DUA)
└── results/
  └── optimal_parameters.csv # Saved best model hyperparameters
  └── ... # Other result files



## Notebooks Overview

### 1. EDA_and_timeseries.ipynb

**Purpose:**  
- Load and inspect the MDS-UPDRS Part III dataset.
- Clean and preprocess data (handle missing values, outliers, date parsing).
- Explore data distributions, correlations, and patient visit patterns.
- Visualize temporal trends in NP3TOT scores, including by medication state (`PDSTATE`).

**Key Steps:**  
- Data loading and initial inspection.
- Data cleaning (date conversion, missing value handling, outlier removal).
- Exploratory analysis (distributions, correlations, visit statistics).
- Visualization (distributions, heatmaps, time trends).

---

### 2. ML.ipynb

**Purpose:**  
- Preprocess and engineer features for machine learning.
- Train and evaluate regression models to predict NP3TOT at the next patient visit.
- Perform hyperparameter tuning and model comparison.

**Key Steps:**  
- Data cleaning and preprocessing (as above).
- Feature engineering (lag features, time deltas, target shifting).
- Model training (Random Forest, XGBoost, MLP Regressor).
- Hyperparameter tuning (GridSearchCV with GroupKFold).
- Evaluation (MAE, MSE, R², visualizations).
- Saving results and best parameters.

---

## Data Source

Both notebooks expect the dataset at: /Users/larsheijnen/Thesis/Final/MDS-UPDRS_Part_III_21Mar2025.csv
If your dataset is elsewhere, update the file path in the notebooks accordingly.

---

**Python Version:**  
- Python 3.8 or higher recommended

**Required Packages:**  
| Package                   | Version   |
|---------------------------|-----------|
| absl-py                   | 2.2.0     |
| anyio                     | 4.9.0     |
| appnope                   | 0.1.4     |
| argon2-cffi               | 23.1.0    |
| argon2-cffi-bindings      | 21.2.0    |
| arrow                     | 1.3.0     |
| asttokens                 | 3.0.0     |
| astunparse                | 1.6.3     |
| async-lru                 | 2.0.5     |
| attrs                     | 25.3.0    |
| babel                     | 2.17.0    |
| beautifulsoup4            | 4.13.3    |
| bleach                    | 6.2.0     |
| certifi                   | 2025.1.31 |
| cffi                      | 1.17.1    |
| charset-normalizer        | 3.4.1     |
| cloudpickle               | 3.1.1     |
| comm                      | 0.2.2     |
| contourpy                 | 1.3.1     |
| cycler                    | 0.12.1    |
| debugpy                   | 1.8.13    |
| decorator                 | 5.2.1     |
| defusedxml                | 0.7.1     |
| executing                 | 2.2.0     |
| factor_analyzer           | 0.5.1     |
| fastjsonschema            | 2.21.1    |
| flatbuffers               | 25.2.10   |
| fonttools                 | 4.56.0    |
| fqdn                      | 1.5.1     |
| gast                      | 0.6.0     |
| google-pasta              | 0.2.0     |
| grpcio                    | 1.71.0    |
| h11                       | 0.14.0    |
| h5py                      | 3.13.0    |
| httpcore                  | 1.0.7     |
| httpx                     | 0.28.1    |
| idna                      | 3.10      |
| imbalanced-learn          | 0.13.0    |
| ipykernel                 | 6.29.5    |
| ipython                   | 9.0.2     |
| ipython_pygments_lexers   | 1.1.1     |
| ipywidgets                | 8.1.5     |
| isoduration               | 20.11.0   |
| jedi                      | 0.19.2    |
| Jinja2                    | 3.1.6     |
| joblib                    | 1.4.2     |
| json5                     | 0.10.0    |
| jsonpointer               | 3.0.0     |
| jsonschema                | 4.23.0    |
| jsonschema-specifications | 2024.10.1 |
| jupyter                   | 1.1.1     |
| jupyter_client            | 8.6.3     |
| jupyter-console           | 6.6.3     |
| jupyter_core              | 5.7.2     |
| jupyter-events            | 0.12.0    |
| jupyter-lsp               | 2.2.5     |
| jupyter_server            | 2.15.0    |
| jupyter_server_terminals  | 0.5.3     |
| jupyterlab                | 4.3.6     |
| jupyterlab_pygments       | 0.3.0     |
| jupyterlab_server         | 2.27.3    |
| jupyterlab_widgets        | 3.0.13    |
| keras                     | 3.9.0     |
| kiwisolver                | 1.4.8     |
| libclang                  | 18.1.1    |
| lightgbm                  | 4.6.0     |
| llvmlite                  | 0.44.0    |
| Markdown                  | 3.7       |
| markdown-it-py            | 3.0.0     |
| MarkupSafe                | 3.0.2     |
| matplotlib                | 3.10.1    |
| matplotlib-inline         | 0.1.7     |
| mdurl                     | 0.1.2     |
| missingno                 | 0.5.2     |
| mistune                   | 3.1.3     |
| ml_dtypes                 | 0.5.1     |
| mlxtend                   | 0.23.4    |
| namex                     | 0.0.8     |
| narwhals                  | 1.31.0    |
| nbclient                  | 0.10.2    |
| nbconvert                 | 7.16.6    |
| nbformat                  | 5.10.4    |

Install all dependencies with:
pip install \
  absl-py anyio appnope argon2-cffi argon2-cffi-bindings arrow asttokens astunparse async-lru attrs \
  babel beautifulsoup4 bleach certifi cffi charset-normalizer cloudpickle comm contourpy cycler debugpy decorator \
  defusedxml executing factor_analyzer fastjsonschema flatbuffers fonttools fqdn gast google-pasta grpcio h11 h5py \
  httpcore httpx idna imbalanced-learn ipykernel ipython ipython_pygments_lexers ipywidgets isoduration jedi Jinja2 \
  joblib json5 jsonpointer jsonschema jsonschema-specifications jupyter jupyter_client jupyter-console jupyter_core \
  jupyter-events jupyter-lsp jupyter_server jupyter_server_terminals jupyterlab jupyterlab_pygments jupyterlab_server \
  jupyterlab_widgets keras kiwisolver libclang lightgbm llvmlite Markdown markdown-it-py MarkupSafe matplotlib \
  matplotlib-inline mdurl missingno mistune ml_dtypes mlxtend namex narwhals nbclient nbconvert nbformat


## Setup & Usage

1. **Clone this repository** (or copy the notebooks and dataset to your working directory).

2. **Install dependencies** (see [Dependencies](#dependencies) section above).

3. **Ensure the dataset is available** at the specified path, or update the file path in the notebooks.

4. **Open and run the notebooks:**
- EDA_and_timeseries.ipynb for data exploration and visualization.
- ML.ipynb for machine learning modeling and evaluation.

## Reproducibility

- The notebooks are designed to be run top-to-bottom, cell by cell.
- For consistent results, use the same Python and package versions as listed in the output of `!pip list` in `ML.ipynb`.
- Random seeds are set where applicable for reproducibility of model results.

## Notes

- The dataset is not included in this repository due to privacy or size constraints.
- Update file paths in the notebooks if your directory structure differs.
- Results (e.g., best hyperparameters, model performance) are saved in the `results/` directory.
- For any issues or questions, please refer to the comments in the notebooks or open an issue.
