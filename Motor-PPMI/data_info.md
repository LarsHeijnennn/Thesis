## Motor Features
| Feature       | Description                     |
|---------------|---------------------------------|
| PATNO         | Identifying information         |
| EVENT_ID      | Identifying information         |
| INFODT        | Identifying information         |
| NP3SPCH       | MDS-UPDRS Part III: Speech      |
| NP3FACXP      | MDS-UPDRS Part III: Facial expression |
| NP3RIGN       | MDS-UPDRS Part III: Rigidity    |
| NP3RIGRU      | MDS-UPDRS Part III: Rigidity (Right Upper Limb) |
| NP3RIGLU      | MDS-UPDRS Part III: Rigidity (Left Upper Limb) |
| NP3RIGRL      | MDS-UPDRS Part III: Rigidity (Right Lower Limb) |
| NP3RIGLL      | MDS-UPDRS Part III: Rigidity (Left Lower Limb) |
| NP3FTAPR      | MDS-UPDRS Part III: Finger tapping (Right) |
| NP3FTAPL      | MDS-UPDRS Part III: Finger tapping (Left) |
| NP3HMOVR      | MDS-UPDRS Part III: Hand movements (Right) |
| NP3HMOVL      | MDS-UPDRS Part III: Hand movements (Left) |
| NP3PRSPR      | MDS-UPDRS Part III: Pronation-supination (Right) |
| NP3PRSPL      | MDS-UPDRS Part III: Pronation-supination (Left) |
| NP3TTAPR      | MDS-UPDRS Part III: Toe tapping (Right) |
| NP3TTAPL      | MDS-UPDRS Part III: Toe tapping (Left) |
| NP3LGAGR      | MDS-UPDRS Part III: Leg agility (Right) |
| NP3LGAGL      | MDS-UPDRS Part III: Leg agility (Left) |
| NP3RISNG      | MDS-UPDRS Part III: Arising from chair |
| NP3GAIT       | MDS-UPDRS Part III: Gait        |
| NP3FRZGT      | MDS-UPDRS Part III: Freezing of gait |
| NP3PSTBL      | MDS-UPDRS Part III: Postural stability |
| NP3POSTR      | MDS-UPDRS Part III: Posture     |
| NP3BRADY      | MDS-UPDRS Part III: Body bradykinesia |
| NP3PTRMR      | MDS-UPDRS Part III: Postural tremor (Right) |
| NP3PTRML      | MDS-UPDRS Part III: Postural tremor (Left) |
| NP3KTRMR      | MDS-UPDRS Part III: Kinetic tremor (Right) |
| NP3KTRML      | MDS-UPDRS Part III: Kinetic tremor (Left) |
| NP3RTARU      | MDS-UPDRS Part III: Rest tremor (Right Upper Limb) |
| NP3RTALU      | MDS-UPDRS Part III: Rest tremor (Left Upper Limb) |
| NP3RTARL      | MDS-UPDRS Part III: Rest tremor (Right Lower Limb) |
| NP3RTALL      | MDS-UPDRS Part III: Rest tremor (Left Lower Limb) |
| NP3RTALJ      | MDS-UPDRS Part III: Rest tremor (Jaw) |
| NP3RTCON      | MDS-UPDRS Part III: Rest tremor (Constancy) |
| NP3TOT        | MDS-UPDRS Part III: Total score |

## Shape and Metrics on Data

At first, we have 32,346 rows and 37 features to consider.

| Metric               | Value   |
|----------------------|---------|
| Variance of NP3TOT   | 215.60  |
| Median of NP3TOT     | 15.00   |
| Mean of NP3TOT       | 16.87   |
| Max of NP3TOT        | 100.00  |
| Min of NP3TOT        | 0.00    |

This shows considerable variance (215.60), meaning NP3TOT scores are spread out widely around the mean. The median being lower than the mean indicates right-skewed data, influenced by a few extremely high values (up to 100). Although most scores fall within 15–17, these outliers significantly raise the mean and variance, resulting in a wide range between the minimum and maximum values.

| Feature     | Missing (%) | Feature     | Missing (%) |
|-------------|-------------|-------------|-------------|
| NP3TOT      | 19.28       | NP3RTARU    | 5.33        |
| NP3TTAPR    | 5.42        | NP3RISNG    | 5.33        |
| NP3PSTBL    | 5.42        | NP3RTARL    | 5.33        |
| NP3TTAPL    | 5.41        | NP3RIGLU    | 5.33        |
| NP3FRZGT    | 5.37        | NP3RTALU    | 5.33        |
| NP3RIGLL    | 5.35        | NP3PRSPR    | 5.33        |
| NP3HMOVL    | 5.34        | NP3GAIT     | 5.33        |
| NP3RTCON    | 5.34        | NP3LGAGL    | 5.33        |
| NP3RIGRL    | 5.34        | NP3FTAPR    | 5.33        |
| NP3FTAPL    | 5.34        | NP3HMOVR    | 5.33        |
| NP3KTRMR    | 5.34        | NP3LGAGR    | 5.33        |
| NP3PTRML    | 5.34        | NP3FACXP    | 5.32        |
| NP3PRSPL    | 5.34        | NP3SPCH     | 5.32        |
| NP3RTALJ    | 5.34        | EVENT_ID    | 0.00        |
| NP3RIGRU    | 5.33        | INFODT      | 0.00        |
| NP3RIGN     | 5.33        | PATNO       | 0.00        |
| NP3KTRML    | 5.33        |             |             |
| NP3RTALL    | 5.33        |             |             |
| NP3PTRMR    | 5.33        |             |             |
| NP3BRADY    | 5.33        |             |             |
| NP3POSTR    | 5.33        |             |             |

## Removing NaN values on NP3TOT
After removing missing values, we keep 26109 rows of the 32,346 rows.

## Check correlation between Time Progression and NP3TOT
-0.09 indicates that there is a very weak negative correlation, almost no relationship. As time moves on, the NP3TOT value slightly decreases.