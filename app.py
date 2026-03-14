import streamlit as st
import pandas as pd
import joblib

# loading model

pipeline = joblib.load('pipeline.pkl')
le = joblib.load('label_encoder.pkl')
cols = joblib.load('col_names.pkl')

# app ui

st.title("Buy's Computer Prediction")
st.write("Priyam Bhattacharya")

# user input

age = st.selectbox(
    "Age",
    ['youth', 'middle_age', 'senior']
)

inc = st.selectbox(
    'Income',
    ['high', 'medium', 'low']
)

student = st.selectbox(
    "Student",
    ['yes', 'no']
)
cr = st.selectbox(
    "Credit Rating",
    ['fair', 'excellent']
)

if st.button("Predict"):
    # dataframe creation
    ns = pd.DataFrame({
        'age': [age],
        'income': [inc],
        'student': [student],
        'credit_rating': [cr]
    })

    ns = ns[cols]

    pred = pipeline.predict(ns)
    res = le.inverse_transform(pred)
    if pred[0] == 1:
        st.success("The person is likely to buy a computer")
    else:
        st.error("The person is not likely to buy a computer")
