import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="👨‍💼",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("employee_attrition_model.pkl", "rb") as file:
        model = pickle.load(file)

    with open("model_features.pkl", "rb") as file:
        features = pickle.load(file)

    return model, features


model, features = load_model()

st.title("👨‍💼 Employee Attrition Prediction")
st.write(
    "Enter employee information to estimate whether the employee "
    "is likely to leave the organization."
)

st.divider()

st.subheader("Employee Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=30,
    step=1
)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=100,
    max_value=50000,
    value=5000,
    step=100
)

overtime = st.selectbox(
    "OverTime",
    ["No", "Yes"]
)

years_at_company = st.number_input(
    "Years at Company",
    min_value=0,
    max_value=50,
    value=5,
    step=1
)

total_working_years = st.number_input(
    "Total Working Years",
    min_value=0,
    max_value=50,
    value=8,
    step=1
)

years_with_manager = st.number_input(
    "Years With Current Manager",
    min_value=0,
    max_value=30,
    value=3,
    step=1
)

st.divider()

if st.button("Predict Attrition", use_container_width=True):

    if years_at_company > total_working_years:
        st.error(
            "Years at Company cannot be greater than Total Working Years."
        )
        st.stop()

    if years_with_manager > years_at_company:
        st.error(
            "Years With Current Manager cannot be greater than Years at Company."
        )
        st.stop()

    overtime_value = 1 if overtime == "Yes" else 0

    new_employee = pd.DataFrame([{
        "MonthlyIncome": monthly_income,
        "OverTime_Yes": overtime_value,
        "YearsAtCompany": years_at_company,
        "TotalWorkingYears": total_working_years,
        "Age": age,
        "YearsWithCurrManager": years_with_manager
    }])

    # Ensure the input columns exactly match the features
    # used while training the final model.
    new_employee = new_employee[features]

    prediction = model.predict(new_employee)[0]
    probability = model.predict_proba(new_employee)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🔴 Employee is likely to leave")
    else:
        st.success("🟢 Employee is likely to stay")

    st.metric(
        "Attrition Probability",
        f"{probability * 100:.2f}%"
    )

    st.caption(
        "This prediction is a machine learning estimate and should be "
        "used as a decision-support signal rather than the sole basis "
        "for HR decisions."
    )
