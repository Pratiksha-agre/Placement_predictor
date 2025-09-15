import streamlit as st
import pickle

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Web app UI
st.title('Placement Predictor')

iq = st.number_input('Enter IQ Score')
cgpa = st.number_input('Enter CGPA')

if st.button('Predict'):
    data = [[iq, cgpa]]
    prediction = model.predict(data)
    if prediction[0] == 1:
        st.success('Placement Ho Jaayega 🚀')
    else:
        st.warning('Placement nahi hua...😔')
