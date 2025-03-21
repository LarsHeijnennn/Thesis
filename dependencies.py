import os

# Install necessary libraries for data analysis and machine learning
# You can run this script in your terminal or Jupyter Notebook


# List of libraries to install
libraries = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "scipy",
    "statsmodels",
    "xgboost",
    "lightgbm",
    "tensorflow",
    "keras",
    "pytorch",
    "jupyter",
    "notebook",
    "plotly",
    "mlxtend",
    "imbalanced-learn",
]

# Install each library
for library in libraries:
    os.system(f"pip install {library}")