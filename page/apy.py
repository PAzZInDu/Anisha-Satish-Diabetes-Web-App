import streamlit as st
import numpy as np
import pickle
from functions import bmi_calculator


# -----------------------------
# Class list as tuples
# -----------------------------
Age = ('Less then 11', 'Less then 15', 'Less then 5', 'greater then 15')
Sex = ('Female', 'Male')
Area_of_Residence  = ('Rural', 'Suburban', 'Urban')
HbA1c = ('Less then 7.5%', 'Over 7.5%')
Adequate_Nutrition  = ('No', 'Yes')
Education_of_Mother = ('No', 'Yes')
Standardized_growth_rate_infancy = ('Highest quartiles', 'Lowest quartiles', 'Middle quartiles')
Standardized_birth_weight = ('Highest quartiles', 'Lowest quartiles', 'Middle quartiles', 'unkhown')
Autoantibodies = ('No', 'Yes')
Impaired_glucose_metabolism  = ('No', 'Yes')
Family_History_affected_Type_1_Diabetes = ('No', 'Yes')
Family_History_affected_type_2_Diabetes = ('No', 'Yes')
Hypoglycemis = ('No', 'Yes')
pancreatic_disease_affected_child  = ('No', 'Yes')

MODEL_NAME = "randomforest_model"
OH_ENCODER = "onehotencoder"


# -----------------------------
# Load model + encoder
# -----------------------------
@st.cache_resource
def load_model(model_name):
    with open(model_name, "rb") as file_name:
        return pickle.load(file_name)

tabular_model = load_model(MODEL_NAME)
one_hot_encoder = load_model(OH_ENCODER)


# -----------------------------
# Title & dashboard
# -----------------------------
st.title("Diabetic Prediction")
st.subheader("User Dashboard")
st.image("https://www.chenmed.com/sites/default/files/styles/blog_post_teaser/public/2023-09/Caring%20for%20Our%20Patients-%20Helping%20an%20Uncontrolled%20Diabetic%20Stay%20Out%20of%20the%20Hospital.jpg?itok=8JOkAalx")


# -----------------------------
# Inputs (stored in session_state automatically)
# -----------------------------
st.info("Please Enter the Following Details")
st.selectbox('Choose Age Category:', Age, index=None, key="age")
st.selectbox('Choose Gender:', Sex, index=None, key="gender")
st.selectbox('Area of Residence:', Area_of_Residence, index=None, key="residence")
st.selectbox('HbA1c Level:', HbA1c, index=None, key="hba1c")
st.selectbox('Adequate Nutrition:', Adequate_Nutrition, index=None, key="nutrition")
st.selectbox("Education of Mother:", Education_of_Mother, index=None, key="mother_education")
st.selectbox("Standardized Growth Rate (Infancy):", Standardized_growth_rate_infancy, index=None, key="growth_rate")
st.selectbox("Standardized Birth Weight:", Standardized_birth_weight, index=None, key="birth_weight")
st.selectbox("Autoantibodies:", Autoantibodies, index=None, key="autoantibodies")
st.selectbox("Impaired Glucose Metabolism:", Impaired_glucose_metabolism, index=None, key="glucose_metabolism")

# Columns removed
st.session_state["insulin_taken"] = "No"
st.session_state["how_taken"] = "No"

st.selectbox("Family History of Type 1 Diabetes:", Family_History_affected_Type_1_Diabetes, index=None, key="family_history_type1")
st.selectbox("Family History of Type 2 Diabetes:", Family_History_affected_type_2_Diabetes, index=None, key="family_history_type2")
st.selectbox("Hypoglycemia:", Hypoglycemis, index=None, key="hypoglycemia")
st.selectbox("Pancreatic Disease Affected Child:", pancreatic_disease_affected_child, index=None, key="pancreatic_disease")

st.number_input("Enter your height in cm", min_value=50, max_value=250, step=1, key="height")
st.number_input("Enter your weight in kg", min_value=10, max_value=200, step=1, key="weight")


# -----------------------------
# Buttons
# -----------------------------
if st.button("Predict"):
    required_fields = [
        "age", "gender", "residence", "hba1c", "nutrition",
        "mother_education", "growth_rate", "birth_weight",
        "autoantibodies", "glucose_metabolism",
        "family_history_type1", "family_history_type2",
        "hypoglycemia", "pancreatic_disease",
        "height", "weight"
    ]

    # Check for missing fields
    missing = [f for f in required_fields if not st.session_state.get(f)]
    if missing:
        st.error("⚠️ Please fill in all fields before making a prediction.")
    else:
        # Calculate BMI
        bmi = bmi_calculator(st.session_state.weight, st.session_state.height)

        # Collect inputs
        user_inputs = [
            st.session_state.age,
            st.session_state.gender,
            st.session_state.residence,
            st.session_state.hba1c,
            st.session_state.nutrition,
            st.session_state.mother_education,
            st.session_state.growth_rate,
            st.session_state.birth_weight,
            st.session_state.autoantibodies,
            st.session_state.glucose_metabolism,
            st.session_state.insulin_taken,
            st.session_state.how_taken,
            st.session_state.family_history_type1,
            st.session_state.family_history_type2,
            st.session_state.hypoglycemia,
            st.session_state.pancreatic_disease
        ]

        user_inputs_arr = np.array([user_inputs])
        ohe_inputs = one_hot_encoder.transform(user_inputs_arr)
        ohe_inputs_new = np.delete(ohe_inputs, [16, 17], axis=1)
        ohe_inputs_new_bmi = np.append(ohe_inputs_new, [[bmi]], axis=1)

        prediction = tabular_model.predict(ohe_inputs_new_bmi)

        if prediction == 0:
            st.success('✅ You are NOT classified as Diabetic')
        else:
            st.warning("🚨 You are classified as Diabetic. Please meet your doctor !!")

if st.button("Reset", type="primary"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
