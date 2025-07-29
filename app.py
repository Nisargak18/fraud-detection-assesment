import streamlit as st
import pickle

# Load model
model = pickle.load(open("fraud_rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Streamlit UI
st.title("Fraud Detection")
amount = st.number_input("Amount")
step = st.number_input("Step")
# ...other inputs...

if st.button("Predict"):
    # Prepare input
    input_data = [[step, amount, ...]]
    scaled = scaler.transform(input_data)
    prediction = model.predict(scaled)
    st.success("Fraud" if prediction[0] == 1 else "Not Fraud")
