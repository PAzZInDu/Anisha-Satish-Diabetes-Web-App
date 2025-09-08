import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Questionnare
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
Insulin_taken = ('No', 'Yes')
How_Taken = ('Injection', 'No')
Family_History_affected_Type_1_Diabetes = ('No', 'Yes')
Family_History_affected_type_2_Diabetes = ('No', 'Yes')
Hypoglycemis = ('No', 'Yes')
pancreatic_disease_affected_child  = ('No', 'Yes')


#MODEL_NAME = "age_detector_model"

# @st.cache_resource
# def load_model(model_name):
#     with open(model_name, "rb") as file_name:
#         return pickle.load(file_name)


#load the model
#tabular_model = load_model(MODEL_NAME)

#creating the web app

#title
st.title("Diabetic Prediction")

#dashboard
st.subheader("User Dashboard")

# User Input
age = st.selectbox(
    'Choose Age Category:',
    Age,
    index=None  
    )

gender = st.selectbox(
    'Choose Gender:',
    Sex,
    index=None  
    )

residence = st.selectbox(
    'Area of Residence:',
    Area_of_Residence,
    index=None  
    )

hba1c = st.selectbox(
    'HbA1c Level:',
    HbA1c,
    index=None
)

nutrition = st.selectbox(
    'Adequate Nutrition:',
    Adequate_Nutrition,
    index=None
)

mother_education = st.selectbox(
    "Education of Mother:",
    Education_of_Mother,
    index=None
)

growth_rate = st.selectbox(
    "Standardized Growth Rate (Infancy):",
    Standardized_growth_rate_infancy,
    index=None
)

birth_weight = st.selectbox(
    "Standardized Birth Weight:",
    Standardized_birth_weight,
    index=None
)

autoantibodies = st.selectbox(
    "Autoantibodies:",
    Autoantibodies,
    index=None
)

glucose_metabolism = st.selectbox(
    "Impaired Glucose Metabolism:",
    Impaired_glucose_metabolism,
    index=None
)

insulin_taken = st.selectbox(
    "Insulin Taken:",
    Insulin_taken,
    index=None
)

how_taken = st.selectbox(
    "How Insulin Taken:",
    How_Taken,
    index=None
)

family_history_type1 = st.selectbox(
    "Family History of Type 1 Diabetes:",
    Family_History_affected_Type_1_Diabetes,
    index=None
)

family_history_type2 = st.selectbox(
    "Family History of Type 2 Diabetes:",
    Family_History_affected_type_2_Diabetes,
    index=None
)

hypoglycemia = st.selectbox(
    "Hypoglycemia:",
    Hypoglycemis,
    index=None
)

pancreatic_disease = st.selectbox(
    "Pancreatic Disease Affected Child:",
    pancreatic_disease_affected_child,
    index=None
)


user_inputs = [
    age,
    gender,
    residence,
    hba1c,
    nutrition,
    mother_education,
    growth_rate,
    birth_weight,
    autoantibodies,
    glucose_metabolism,
    insulin_taken,
    how_taken,
    family_history_type1,
    family_history_type2,
    hypoglycemia,
    pancreatic_disease
]


# App

