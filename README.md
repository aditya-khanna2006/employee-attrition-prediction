# Employee Attrition Prediction Using Machine Learning

An end-to-end machine learning project that predicts whether an employee is likely to leave an organization based on selected employee-related factors.

## 🌐 Live Demo

Try the deployed Employee Attrition Prediction application:

👉 **[Open Live Streamlit App](https://employee-attrition-ml-prediction.streamlit.app/)**

### 📸 Application Preview

<img width="495" height="817" alt="Screenshot 2026-09-14 225157" src="https://github.com/user-attachments/assets/cad0db41-8284-4db6-961d-7a956f57ddb5" />

<img width="536" height="822" alt="Screenshot 2026-09-14 225116" src="https://github.com/user-attachments/assets/b81e1177-9255-45a8-85c0-12891b17401d" />

---

## 📌 Project Overview

Employee attrition can create significant challenges for organizations, including recruitment costs, training requirements, productivity loss, reduced productivity, and workforce instability.

This project develops a machine learning-based system to estimate employee attrition risk.

The trained machine learning model is integrated with a Streamlit web application where users can enter employee information and receive:

- Employee attrition prediction
- Estimated attrition probability

The project is developed as a BCA Minor Project with a focus on practical machine learning implementation, model evaluation, explainability, and deployment.

---

## 🎯 Objectives

- Analyze employee attrition patterns using data.
- Perform data cleaning and preprocessing.
- Explore relationships between employee characteristics and attrition.
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

---

## 📊 Dataset

The project uses the **IBM HR Analytics Employee Attrition & Performance** dataset.

### Dataset Information

| Property | Value |
|---|---|
| Total Records | 1,470 |
| Original Features | 35 |
| Target Variable | `Attrition` |
| Target Classes | `Yes`, `No` |

The dataset contains employee demographic, job-related, income, experience, and work-related information.

---

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
New Employee Prediction
   ↓
Public Deployment
```

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Checked dataset dimensions and data types.
- Checked missing values.
- Checked duplicate records.
- Removed non-predictive columns.
- Converted categorical variables using one-hot encoding.
- Used stratified train-test splitting.
- Selected important features using feature importance.

### Outlier Analysis

Outliers were examined using statistical and visual techniques.

Extreme values were not removed arbitrarily when they represented plausible employee characteristics. This approach helps avoid unnecessary information loss.

---

## ⚖️ Handling Class Imbalance

The target variable is imbalanced because the number of employees who stayed is considerably higher than the number of employees who left.

To address this issue:

- Stratified train-test splitting was used.
- Balanced class weights were applied during model training.
- Accuracy was not considered as the only evaluation metric.
- Precision, Recall, F1-Score, and ROC-AUC were also evaluated.

F1-Score was given particular importance because the target classes are imbalanced.

---

## 🤖 Machine Learning Models

The following classification models were trained and evaluated:

1. **Logistic Regression**
2. **Decision Tree**
3. **Random Forest**
4. **Tuned Random Forest**

The Random Forest model was further optimized using **GridSearchCV**.

### Hyperparameter Tuning

GridSearchCV was used to search for suitable values of:

- Number of estimators
- Maximum tree depth
- Minimum samples per leaf

**F1-Score** was used as the optimization metric.

---

## 🔍 Feature Selection

Feature importance was calculated using a Random Forest model trained on the training data.

The final prediction model uses the following six important features:

| Feature | Description |
|---|---|
| `MonthlyIncome` | Employee monthly income |
| `OverTime_Yes` | Whether the employee works overtime |
| `YearsAtCompany` | Number of years the employee has worked at the company |
| `TotalWorkingYears` | Total professional working experience |
| `Age` | Employee age |
| `YearsWithCurrManager` | Years working with the current manager |

Using a smaller set of important features makes the final prediction model more compact, interpretable, and suitable for deployment.

---

## 📏 Model Evaluation

The models were evaluated using multiple performance metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix
- Stratified Cross-Validation

Since the target variable is imbalanced, multiple evaluation metrics were considered instead of relying only on accuracy.

---

## 🔎 Model Explainability — SHAP

**SHAP (SHapley Additive exPlanations)** was used to analyze the contribution of features to the model's predictions.

SHAP helps understand how the selected employee features influence the model's output.

This improves the interpretability of the machine learning model and provides additional insight into the factors contributing to employee attrition predictions.

---

## 💾 Model Saving and Loading

The final trained model is saved as:

```text
employee_attrition_model.pkl
```

The feature order required by the model is stored as:

```text
model_features.pkl
```

These files allow the trained model to be loaded and used for predictions without retraining it.

---

## 🌐 Streamlit Application

An interactive **Streamlit** web application was developed to use the trained model.

### Input Features

Users can enter:

- Age
- Monthly Income
- OverTime
- Years at Company
- Total Working Years
- Years With Current Manager

### Application Output

The application provides:

- Predicted attrition status
- Estimated attrition probability

### Application Flow

```text
Employee Information
        ↓
   Input Validation
        ↓
   Trained ML Model
        ↓
    Prediction
        ↓
Attrition Probability
```

The application also performs basic validation to prevent logically inconsistent inputs.

For example:

- Years at Company cannot be greater than Total Working Years.
- Years With Current Manager cannot be greater than Years at Company.

---

## 🚀 Deployment

The Streamlit application has been deployed publicly using **Streamlit Community Cloud**.

### 🔗 Live Application

👉 **[Employee Attrition Prediction — Live App](https://employee-attrition-ml-prediction.streamlit.app/)**

The deployed application loads the saved machine learning model and feature configuration and performs predictions for new employee inputs.

---

## 📁 Project Structure

```text
employee-attrition-prediction/
│
├── images/
│   ├── stay_prediction.png
│   └── leave_prediction.png
│
├── Employee_Attrition_Prediction.ipynb
├── app.py
├── employee_attrition_model.pkl
├── model_features.pkl
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Description |
|---|---|
| `images/` | Screenshots of the Streamlit application |
| `Employee_Attrition_Prediction.ipynb` | Complete data analysis, preprocessing, feature selection, model training, evaluation, SHAP analysis, and model saving workflow |
| `app.py` | Streamlit web application |
| `employee_attrition_model.pkl` | Saved trained machine learning model |
| `model_features.pkl` | Saved feature order required by the model |
| `requirements.txt` | Required Python libraries |
| `README.md` | Project documentation |

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**
- **SHAP**
- **Jupyter Notebook**
- **Streamlit**
- **GitHub**

---

## 💻 Running the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/aditya-khanna2006/employee-attrition-prediction.git
```

### 2. Navigate to the project directory

```bash
cd employee-attrition-prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

### 5. Open the application

The application will be available through the local Streamlit URL displayed in the terminal.

---

## 🔮 Future Scope

The project can be further enhanced through:

1. Testing additional machine learning algorithms such as Gradient Boosting and XGBoost.
2. Probability threshold optimization according to specific HR requirements.
3. Integration with a real-time HR database.
4. Continuous monitoring of model performance after deployment.
5. Adding authentication and role-based access.
6. Providing personalized prediction explanations for HR users.
7. Periodic retraining of the model using updated employee data.
8. Monitoring model fairness and potential bias across different employee groups.

---

## 👨‍💻 Project Team

### Aditya Khanna

**BCA | Data Analytics & Machine Learning**

GitHub: [aditya-khanna2006](https://github.com/aditya-khanna2006)

### Anuj Dubey

**BCA | Data Analytics & Machine Learning**

---

## 📌 Project Type

**BCA Minor Project — Team Project**

---

## ⚠️ Disclaimer

This project is developed for academic and educational purposes.

The predictions generated by the application are machine learning estimates based on the provided dataset and should not be treated as definitive decisions about individual employees.

The system is intended to act as a decision-support tool rather than replace human judgment in HR-related decisions.
