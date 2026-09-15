import streamlit as st
import pandas as pd
import pickle

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Hero Header */

.hero {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(135deg, #1f4e79, #2563eb);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 17px;
    opacity: 0.9;
}


/* Section Titles */

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 15px;
}


/* Result Card */

.result-card {
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid rgba(128,128,128,0.25);
    margin-bottom: 15px;
}

.result-title {
    font-size: 27px;
    font-weight: 700;
    margin-bottom: 8px;
}


/* Risk Badge */

.risk-badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 12px;
}


/* Info Cards */

.info-card {
    padding: 18px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.25);
    margin-bottom: 12px;
}

.info-label {
    font-size: 13px;
    opacity: 0.7;
}

.info-value {
    font-size: 21px;
    font-weight: 700;
}


/* Footer */

.footer {
    text-align: center;
    opacity: 0.65;
    padding-top: 35px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SESSION STATE FOR RESET
# --------------------------------------------------

if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0


reset_key = st.session_state.reset_counter


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():

    with open("employee_attrition_model.pkl", "rb") as file:
        model = pickle.load(file)

    with open("model_features.pkl", "rb") as file:
        features = pickle.load(file)

    return model, features


model, features = load_model()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("⚙️ Project Information")

    st.markdown("---")

    st.markdown("### 🤖 Machine Learning")

    st.write("**Model:** Random Forest")
    st.write("**Task:** Binary Classification")
    st.write("**Target:** Employee Attrition")

    st.markdown("---")

    st.markdown("### 📊 Selected Features")

    st.write("• Monthly Income")
    st.write("• OverTime")
    st.write("• Years at Company")
    st.write("• Total Working Years")
    st.write("• Age")
    st.write("• Years With Current Manager")

    st.markdown("---")

    st.markdown("### 👨‍💻 Project Team")

    st.write("**Aditya Khanna**")
    st.write("**Anuj Dubey**")

    st.markdown("---")

    st.caption(
        "BCA Minor Project\n\n"
        "Employee Attrition Prediction Using Machine Learning"
    )


# --------------------------------------------------
# HERO HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">

<h1>👨‍💼 Employee Attrition Predictor</h1>

<p>
Machine Learning based system for estimating employee attrition risk
using selected employee characteristics.
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# EMPLOYEE INFORMATION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">👤 Employee Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30,
        step=1,
        key=f"age_{reset_key}",
        help="Employee age in years."
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=100,
        max_value=50000,
        value=5000,
        step=100,
        key=f"income_{reset_key}",
        help="Employee monthly income."
    )

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"],
        key=f"overtime_{reset_key}",
        help="Whether the employee works overtime."
    )


with col2:

    years_at_company = st.number_input(
        "Years at Company",
        min_value=0,
        max_value=50,
        value=5,
        step=1,
        key=f"company_years_{reset_key}",
        help="Number of years the employee has worked at the company."
    )

    total_working_years = st.number_input(
        "Total Working Years",
        min_value=0,
        max_value=50,
        value=8,
        step=1,
        key=f"total_years_{reset_key}",
        help="Total professional working experience."
    )

    years_with_manager = st.number_input(
        "Years With Current Manager",
        min_value=0,
        max_value=30,
        value=3,
        step=1,
        key=f"manager_years_{reset_key}",
        help="Number of years working with the current manager."
    )


st.markdown("---")


# --------------------------------------------------
# EMPLOYEE PROFILE
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📋 Employee Profile</div>',
    unsafe_allow_html=True
)

summary1, summary2, summary3, summary4 = st.columns(4)


with summary1:
    st.metric(
        "Age",
        f"{age} years"
    )


with summary2:
    st.metric(
        "Monthly Income",
        f"₹{monthly_income:,}"
    )


with summary3:
    st.metric(
        "Company Experience",
        f"{years_at_company} years"
    )


with summary4:
    st.metric(
        "OverTime",
        overtime
    )


st.markdown("<br>", unsafe_allow_html=True)


# --------------------------------------------------
# BUTTONS
# --------------------------------------------------

predict_col, reset_col = st.columns([3, 1])


with predict_col:

    predict_button = st.button(
        "🚀 Predict Attrition",
        use_container_width=True,
        type="primary"
    )


with reset_col:

    reset_button = st.button(
        "🔄 Reset",
        use_container_width=True
    )


# --------------------------------------------------
# RESET
# --------------------------------------------------

if reset_button:

    st.session_state.reset_counter += 1

    st.rerun()


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if predict_button:

    # ----------------------------------------------
    # VALIDATION
    # ----------------------------------------------

    if years_at_company > total_working_years:

        st.error(
            "❌ Years at Company cannot be greater than "
            "Total Working Years."
        )

        st.stop()


    if years_with_manager > years_at_company:

        st.error(
            "❌ Years With Current Manager cannot be greater "
            "than Years at Company."
        )

        st.stop()


    # ----------------------------------------------
    # OVERTIME CONVERSION
    # ----------------------------------------------

    overtime_value = 1 if overtime == "Yes" else 0


    # ----------------------------------------------
    # CREATE EMPLOYEE DATA
    # ----------------------------------------------

    new_employee = pd.DataFrame([{

        "MonthlyIncome": monthly_income,

        "OverTime_Yes": overtime_value,

        "YearsAtCompany": years_at_company,

        "TotalWorkingYears": total_working_years,

        "Age": age,

        "YearsWithCurrManager": years_with_manager

    }])


    # ----------------------------------------------
    # ARRANGE FEATURES
    # ----------------------------------------------

    new_employee = new_employee[features]


    # ----------------------------------------------
    # MODEL PREDICTION
    # ----------------------------------------------

    prediction = model.predict(new_employee)[0]

    probability = model.predict_proba(new_employee)[0][1]

    probability_percent = probability * 100


    # ----------------------------------------------
    # RISK LEVEL
    # ----------------------------------------------

    if probability_percent < 30:

        risk_level = "LOW RISK"
        risk_icon = "🟢"

    elif probability_percent < 60:

        risk_level = "MEDIUM RISK"
        risk_icon = "🟡"

    else:

        risk_level = "HIGH RISK"
        risk_icon = "🔴"


    # ----------------------------------------------
    # RESULT
    # ----------------------------------------------

    st.markdown("---")

    st.markdown(
        '<div class="section-title">🎯 Prediction Result</div>',
        unsafe_allow_html=True
    )


    result_col1, result_col2 = st.columns(2)


    # ----------------------------------------------
    # PREDICTION CARD
    # ----------------------------------------------

    with result_col1:

        if prediction == 1:

            st.markdown(
                f"""
                <div class="result-card">

                <div class="risk-badge">
                {risk_icon} {risk_level}
                </div>

                <div class="result-title">
                🔴 Employee is likely to leave
                </div>

                <p>
                The model estimates a higher likelihood
                of employee attrition.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="result-card">

                <div class="risk-badge">
                {risk_icon} {risk_level}
                </div>

                <div class="result-title">
                🟢 Employee is likely to stay
                </div>

                <p>
                The model estimates a lower likelihood
                of employee attrition.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    # ----------------------------------------------
    # PROBABILITY
    # ----------------------------------------------

    with result_col2:

        st.markdown(
            """
            <div class="result-card">

            <div class="info-label">
            ATTRITION PROBABILITY
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.metric(
            "Probability",
            f"{probability_percent:.2f}%"
        )

        st.progress(probability)


    # ----------------------------------------------
    # INTERPRETATION
    # ----------------------------------------------

    if probability_percent < 30:

        st.info(
            "💡 **Interpretation:** The employee has a relatively "
            "low predicted probability of leaving."
        )

    elif probability_percent < 60:

        st.warning(
            "💡 **Interpretation:** The employee falls into a "
            "moderate attrition-risk range and may require attention."
        )

    else:

        st.error(
            "💡 **Interpretation:** The employee has a relatively "
            "high predicted probability of leaving."
        )


    # ----------------------------------------------
    # MODEL INPUT FACTORS
    # ----------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🔍 Model Input Factors</div>',
        unsafe_allow_html=True
    )


    factor1, factor2, factor3 = st.columns(3)


    with factor1:

        st.markdown(
            f"""
            <div class="info-card">

            <div class="info-label">
            MONTHLY INCOME
            </div>

            <div class="info-value">
            ₹{monthly_income:,}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with factor2:

        st.markdown(
            f"""
            <div class="info-card">

            <div class="info-label">
            OVERTIME
            </div>

            <div class="info-value">
            {overtime}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with factor3:

        st.markdown(
            f"""
            <div class="info-card">

            <div class="info-label">
            YEARS AT COMPANY
            </div>

            <div class="info-value">
            {years_at_company} years
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ----------------------------------------------
    # DISCLAIMER
    # ----------------------------------------------

    st.caption(
        "⚠️ This prediction is a machine learning estimate and "
        "should be used as a decision-support signal rather than "
        "the sole basis for HR decisions."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

Employee Attrition Prediction Using Machine Learning<br>

BCA Minor Project | Aditya Khanna & Anuj Dubey

</div>
""", unsafe_allow_html=True)
