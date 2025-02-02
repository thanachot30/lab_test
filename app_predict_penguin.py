
import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load the saved model
with open("model_penguin.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app
st.title("Penguin Species Prediction App")
st.write("This app predicts the penguin species based on several features.")

# User input
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
culmen_length_mm = st.number_input("Culmen Length (mm)", min_value=0.0)
culmen_depth_mm = st.number_input("Culmen Depth (mm)", min_value=0.0)
flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0.0)
body_mass_g = st.number_input("Body Mass (g)", min_value=0.0)
sex = st.selectbox("Sex", ["MALE", "FEMALE"])

# Prediction
if st.button("Predict Species"):
    # Create a DataFrame from the input
    input_data = pd.DataFrame({
        "island": [island],
        "culmen_length_mm": [culmen_length_mm],
        "culmen_depth_mm": [culmen_depth_mm],
        "flipper_length_mm": [flipper_length_mm],
        "body_mass_g": [body_mass_g],
        "sex": [sex]
    })

    # Predict species
    prediction = model.predict(input_data)
    st.write(f"Predicted Species: {prediction[0]}")


