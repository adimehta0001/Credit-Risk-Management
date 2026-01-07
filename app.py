import streamlit as st
import pickle
import pandas as pd
try:
    with open('credit_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model not found! Please run 'train_model.ipynb' first.")
    st.stop()
st.title("🎓 Learning Risk Evaluation Model")
st.write("Enter the details below to predict loan default risk.")
age = st.slider("Applicant Age", 18, 75, 30)
credit_amount = st.slider("Loan Amount ($)", 500, 15000, 5000)
duration = st.slider("Loan Duration (Months)", 6, 72, 24)
if st.button("Calculate Risk"):

    input_data = pd.DataFrame(
        [[age, credit_amount, duration]], 
        columns=['age', 'credit_amount', 'duration']
    )
    prediction = model.predict(input_data)
    if prediction[0] == 'good':
        st.success("✅ LOW RISK: Loan Approved")
    else:
        st.error("⚠️ HIGH RISK: Loan Rejected")