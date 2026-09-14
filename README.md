# Employee Attrition Prediction Using Machine Learning

An end-to-end machine learning project that predicts whether an employee is likely to leave an organization based on selected employee-related factors.

## 📌 Project Overview

Employee attrition can create significant challenges for organizations, including recruitment costs, training requirements, productivity loss, and workforce instability.

This project develops a machine learning-based system to estimate employee attrition risk. The trained model is integrated with a Streamlit web application where users can enter employee information and receive an attrition prediction along with the estimated probability.

The project is developed as a BCA academic project with a focus on practical machine learning implementation, model evaluation, explainability, and deployment.

## 🎯 Objectives

- Analyze employee attrition patterns using data.
- Perform data cleaning and preprocessing.
- Identify important factors related to employee attrition.
- Handle class imbalance during model training.
- Compare multiple machine learning classification models.
- Select important features for a compact prediction model.
- Tune the final Random Forest model.
- Evaluate the model using multiple performance metrics.
- Apply SHAP for model explainability.
- Save and load the trained machine learning model.
- Build an interactive Streamlit prediction application.
- Deploy the application for public access.

## 📊 Dataset

The project uses the IBM HR Analytics Employee Attrition & Performance dataset.

### Dataset Information

- **Records:** 1,470 employees
- **Original Features:** 35
- **Target Variable:** `Attrition`
- **Target Classes:** `Yes` and `No`

The dataset contains employee demographic, job-related, income, experience, and work-related information.

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Outlier Analysis
   ↓
Class Imbalance Analysis
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Feature Selection
   ↓
Model Training
   ↓
Model Comparison
   ↓
Hyperparameter Tuning
   ↓
Cross-Validation
   ↓
Final Model Evaluation
   ↓
SHAP Explainability
   ↓
Model Saving
   ↓
Streamlit Application
   ↓
Prediction for New Employee
```

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Checked dataset dimensions and data types.
- Checked missing values.
- Checked duplicate records.
- Removed non-predictive columns.
- Converted categorical variables using one-hot encoding.
- Used stratified train-test splitting.
- Selected important features using feature importance.

Outliers were examined using statistical and visual techniques. Plausible extreme employee values were retained instead of removing them arbitrarily.

## ⚖️ Handling Class Imbalance

The target variable contains more employees who stayed than employees who left.

To address this issue:

- Stratified train-test splitting was used.
- Balanced class weights were applied during model training.
- Accuracy was not used as the only evaluation metric.
- Precision, Recall, F1-Score, and ROC-AUC were also considered.

## 🤖 Machine Learning Models

The following classification models were evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Tuned Random Forest

The final Random Forest model was tuned using GridSearchCV with F1-Score as the optimization metric.

## 🔍 Selected Features

The final prediction model uses six important features:

| Feature | Description |
|---|---|
| `MonthlyIncome` | Employee monthly income |
| `OverTime_Yes` | Whether the employee works overtime |
| `YearsAtCompany` | Number of years at the company |
| `TotalWorkingYears` | Total professional working experience |
| `Age` | Employee age |
| `YearsWithCurrManager` | Years working with the current manager |

## 📏 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix
- Stratified Cross-Validation

F1-Score was given particular importance because the target variable is imbalanced.

## 🔎 Model Explainability

SHAP (SHapley Additive exPlanations) was used to analyze the contribution of features to the model's predictions.

This helps provide a better understanding of how important employee characteristics influence the model's predictions.

## 💾 Model Saving and Loading

The final trained model is saved as:

```text
employee_attrition_model.pkl
```

The feature order required by the model is stored in:

```text
model_features.pkl
```

These files allow the trained model to be loaded and used for predictions without retraining it.

## 🌐 Streamlit Application

The project includes an interactive Streamlit web application.

Users can enter:

- Age
- Monthly Income
- OverTime
- Years at Company
- Total Working Years
- Years With Current Manager

The application provides:

- Predicted attrition status
- Estimated attrition probability

### Application Flow

```text
Employee Information
        ↓
   Trained ML Model
        ↓
    Prediction
        ↓
Attrition Probability
```

The prediction is intended as a decision-support signal and should not be used as the sole basis for HR decisions.

## 📁 Project Structure

```text
employee-attrition-prediction/
│
├── app.py
├── employee_attrition_model.pkl
├── model_features.pkl
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SHAP
- Jupyter Notebook
- Streamlit
- GitHub

## 🚀 Running the Application Locally

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit application

```bash
streamlit run app.py
```

### 3. Open the application

The application will be available through the local Streamlit URL displayed in the terminal.

## 🔮 Future Scope

The project can be further enhanced through:

1. Testing additional machine learning algorithms such as Gradient Boosting and XGBoost.
2. Probability threshold optimization according to specific HR requirements.
3. Integration with a real-time HR database.
4. Continuous monitoring of model performance after deployment.
5. Adding authentication and role-based access.
6. Providing personalized risk explanations for HR users.
7. Periodic retraining of the model using updated employee data.
8. Monitoring model fairness and potential bias across different employee groups.

## 👨‍💻 Project Team

### Aditya Khanna

BCA | Data Analytics & Machine Learning

GitHub: [aditya-khanna2006](https://github.com/aditya-khanna2006)

### Anuj Dubey

BCA | Data Analytics & Machine Learning

## 📌 Project Type

**BCA Minor Project — Team Project**

## ⚠️ Disclaimer

This project is developed for academic and educational purposes.

The predictions generated by the application are machine learning estimates based on the provided dataset and should not be treated as definitive decisions about individual employees.
