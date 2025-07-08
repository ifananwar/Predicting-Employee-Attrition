# 📊 HR Analytics: Predicting Employee Attrition

## Repository Outline

This repository contains the following files:

1. `README.md` – General overview of the project.  
2. `notebook.ipynb` – Main notebook for data processing and model building.  
3. `inference.ipynb` – Notebook for running inference on new data.  
4. `dataset.csv` – The dataset used for the analysis and modeling.

---

## Problem Background

**HR Analytics** is the process of analyzing human resource data to improve organizational performance. This includes analyzing employees, candidates, and their performance trends. By using HR analytics, organizations gain objective, data-driven evidence of how human capital contributes to success.

Organizational performance is highly dependent on employee quality. One major challenge is **employee attrition**, which creates several negative consequences:

### 🔍 Why is HR Analytics Important?

Employee turnover impacts the organization in many ways:

- 💸 **Training costs** and time for new hires  
- 🧠 Loss of **experience and productivity**  
- 📉 Decrease in **team morale and performance**  
- 💼 Disruption to a stable **work environment**

HR analytics enables organizations to:

- 📈 Detect **patterns among employees likely to leave**  
- 🧑‍💼 Take **proactive and human-centered steps**, such as informal check-ins and stay interviews  
- 🛠️ Conduct **root cause analysis** and implement systemic improvements: career pathing, job rotation, and reward systems

> With this approach, HR evolves from being reactive to turnover to becoming a **strategic partner** in employee retention and organizational growth.

---

## Objective

To develop a classification model that predicts employee attrition using HR analytics. The project is considered successful if the model can detect at least 80% of employees who leave (recall ≥ 0.80), supporting HR in making proactive decisions. The model is expected to be completed within one week by June 18, 2025.

---

## Project Output

Project deliverables:

- Exploratory Data Analysis (EDA)  
- Python-based model inference  
- [Inference Deployment on HuggingFace](https://huggingface.co/spaces/ifananwar/attrition-classifier)

---

## Data

**File:** `dataset.csv`  
**Source:** [Kaggle Dataset - IBM HR Analytics](https://www.kaggle.com/code/faressayah/ibm-hr-analytics-employee-attrition-performance)

| **Column** | **Type** | **Description** |
|------------|----------|-----------------|
| Age | Numeric | Employee’s age |
| Attrition | Categorical (nominal) | Whether the employee left the company |
| BusinessTravel | Categorical (nominal) | Frequency of business travel |
| DailyRate | Numeric | Daily internal rate or cost estimate |
| Department | Categorical (nominal) | Department the employee works in |
| DistanceFromHome | Numeric | Distance from home to office |
| Education | Categorical (ordinal) | Education level (1–5): 1=High School, 5=Doctorate |
| EducationField | Categorical (nominal) | Field of education |
| EmployeeNumber | Numeric (ID) | Unique employee ID |
| EnvironmentSatisfaction | Categorical (ordinal) | Satisfaction with the work environment (1–4) |
| Gender | Categorical (nominal) | Gender (Female, Male) |
| HourlyRate | Numeric | Hourly rate or estimate |
| JobInvolvement | Categorical (ordinal) | Level of job involvement (1–4) |
| JobLevel | Categorical (ordinal) | Job seniority level (1–5) |
| JobRole | Categorical (nominal) | Job role title (e.g., Sales Executive, Manager) |
| JobSatisfaction | Categorical (ordinal) | Job satisfaction (1–4) |
| MaritalStatus | Categorical (nominal) | Marital status (Single, Married, Divorced) |
| MonthlyIncome | Numeric | Monthly salary |
| MonthlyRate | Numeric | Monthly project cost allocation |
| NumCompaniesWorked | Numeric | Number of previous employers |
| OverTime | Categorical (nominal) | Whether the employee works overtime |
| Over18 | Categorical | Whether employee is over 18 (Y/N) |
| PercentSalaryHike | Numeric | Percentage of last salary increase |
| PerformanceRating | Categorical (ordinal) | Performance rating (3=Good, 4=Excellent) |
| RelationshipSatisfaction | Categorical (ordinal) | Satisfaction with work relationships (1–4) |
| StockOptionLevel | Categorical (ordinal) | Stock option level (0–3) |
| TotalWorkingYears | Numeric | Total years of work experience |
| TrainingTimesLastYear | Numeric | Number of trainings in the past year |
| WorkLifeBalance | Categorical (ordinal) | Work-life balance score (1–4) |
| YearsAtCompany | Numeric | Years spent at the current company |
| YearsInCurrentRole | Numeric | Years in current role |
| YearsSinceLastPromotion | Numeric | Years since last promotion |
| YearsWithCurrManager | Numeric | Years working with the current manager |

---

## Method

The methods used in this project include:

- SMART goals for defining the project objective  
- 5W1H for initial data exploration  
- Outlier handling using Turkey's Rule and Z-score  
- Winsorization (capping)  
- Correlation analysis: Kendall and Chi-Square  
- Feature scaling using MinMaxScaler  
- SMOTENC for synthetic data generation  
- Encoding using Ordinal and OneHot Encoding  
- Pipeline creation with `ImbPipeline`  
- Hyperparameter tuning with `RandomizedSearchCV`  
- Classification models used:
  - Logistic Regression  
  - K-Nearest Neighbors (KNN)  
  - Random Forest  
  - Decision Tree  
  - Gradient Boosting  
  - HistGradientBoosting  
  - AdaBoost  
- Evaluation metric: **Recall**

---

## Stacks

**Libraries and tools used:**

- `pandas`  
- `numpy`  
- `matplotlib`, `seaborn`  
- `pickle`  
- `scipy.stats`  
- `sklearn.preprocessing` (LabelEncoder, MinMaxScaler, OneHotEncoder, OrdinalEncoder)  
- `sklearn.model_selection` (train_test_split, RandomizedSearchCV, cross_validate)  
- `sklearn.linear_model` (LogisticRegression)  
- `sklearn.ensemble` (RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, HistGradientBoostingClassifier)  
- `sklearn.neighbors` (KNeighborsClassifier)  
- `sklearn.svm` (SVC)  
- `sklearn.tree` (DecisionTreeClassifier)  
- `sklearn.compose` (ColumnTransformer)  
- `sklearn.metrics` (recall_score)  
- `feature_engine.outliers` (Winsorizer)  
- `imblearn.pipeline` (Pipeline)  
- `imblearn.over_sampling` (SMOTENC)

---

## References

- [IBM HR Analytics 💼 Employee Attrition & Performance – Kaggle](https://www.kaggle.com/code/faressayah/ibm-hr-analytics-employee-attrition-performance)  
- [HR Analytics Prediction: Why do People Resign? – Kaggle](https://www.kaggle.com/code/paramarthasengupta/hr-analytics-prediction-why-do-people-resign)
