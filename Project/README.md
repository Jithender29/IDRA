# Employee Attrition and Workforce Analytics

## Project Overview

This project analyses employee attrition as part of the IDRA Capstone Project 7. It presents an end-to-end data science workflow for understanding which employee, job, and workplace characteristics are associated with employee turnover.

The analysis uses the IBM HR Employee Attrition dataset. It covers data loading, data-quality checks, cleaning, exploratory data analysis (EDA), statistical analysis, feature preparation, machine learning, and model evaluation. The positive class is `Attrition = Yes`.

The results are intended to support HR prioritisation and further investigation. They describe associations in a cross-sectional dataset and should not be interpreted as proof of causation or as a replacement for fair, human-led retention decisions.

## Workflow

1. Load and inspect the raw employee dataset.
2. Check missing values, duplicates, category consistency, valid ranges, and potential outliers.
3. Explore attrition patterns by overtime, job role, income, age, job satisfaction, and other variables.
4. Prepare features with imputation, scaling, and one-hot encoding.
5. Split the data into training and test sets using a fixed random state.
6. Train and compare a dummy baseline, logistic regression, and random forest classifier.
7. Evaluate performance with accuracy, precision, recall, F1 score, ROC-AUC, confusion matrices, and ROC curves.
8. Review model coefficients and communicate practical limitations.

## Files and Directories

| Path | Description |
| --- | --- |
| `Jithender_Reddy_Project7_Employee_Attrition.ipynb` | Main analysis notebook containing data preparation, EDA, statistical analysis, model training, evaluation, and interpretation. |
| `data/P_7_WA_Fn-UseC_-HR-Employee-Attrition.csv` | Original raw HR employee attrition dataset. The notebook reads this file without modifying it. |
| `data/employee_attrition_cleaned.csv` | Cleaned version of the employee attrition dataset produced during preprocessing. |
| `figures/figure_1_attrition_distribution.png` | Overall attrition distribution. |
| `figures/figure_2_overtime_attrition.png` | Attrition comparison for employees with different overtime statuses. |
| `figures/figure_3_job_role_attrition.png` | Attrition rates by job role. |
| `figures/figure_4_income_age_by_attrition.png` | Income and age patterns grouped by attrition status. |
| `figures/figure_5_job_satisfaction_attrition.png` | Relationship between job satisfaction and attrition. |
| `figures/figure_6_correlation_heatmap.png` | Correlation heatmap for selected numeric variables. |
| `figures/figure_7_confusion_matrix.png` | Classification confusion matrix. |
| `figures/figure_8_roc_curve.png` | ROC curve for model evaluation. |
| `figures/figure_9_top_coefficients.png` | Most influential logistic regression coefficients. |
| `Jithender_Reddy_Project7_Employee_Attrition_Report.docx` | Written project report containing the documented findings and conclusions. |

## Running the Notebook

Open `Jithender_Reddy_Project7_Employee_Attrition.ipynb` in Jupyter Notebook or VS Code and run the cells from top to bottom. The notebook expects the `data/` directory to be next to it and creates or updates the charts in `figures/`.

The analysis uses Python with the following main packages:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

The notebook uses `RANDOM_STATE = 42` for reproducible train-test splitting and model results.
