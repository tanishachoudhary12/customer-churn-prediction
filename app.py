# app.py
import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('customer_churn_model.pkl')  # Replace with your actual model filename

# Set title
st.title("Customer Churn Prediction App")

# User input fields
gender = st.selectbox("Gender", ['Female', 'Male'])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ['Yes', 'No'])
Dependents = st.selectbox("Dependents", ['Yes', 'No'])
tenure = st.slider("Tenure (months)", 0, 72)
MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")

# Add more fields depending on your model input...

# Convert inputs to dataframe
input_df = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [SeniorCitizen],
    'Partner': [Partner],
    'Dependents': [Dependents],
    'tenure': [tenure],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges]
    # Add all other required features
})

# Process categorical variables if needed (same encoding as training time)

# Predict
if st.button('Predict'):
    prediction = model.predict(input_df)
    st.write(f'Prediction: {"Churn" if prediction[0] == 1 else "No Churn"}')
