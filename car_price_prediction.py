import streamlit as st
import pickle
import numpy as np

st.header("Car Prediction Application")

col1, col2= st.columns(2)

with col1:
    fuel= col1.selectbox(
    'Select Fuel Type',
    ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'))

with col2:
    transmission= st.radio(
        "Select Transmission 👇",
        ['Manual','Automatic'],
        key="Transmission",
    )

col1, col2= st.columns(2)

with col1:
    engine = col1.slider('Select Engine Power', 500, 5000, step=100)

with col2:
    seats= st.selectbox(
    'Select the no. of seats',
   [4,5,6,7,8,9])

col1, col2= st.columns(2)

with col1:
    make = col1.slider('Select Make Year', 2000, 2020, step=1)

with col2:
    km = col2.slider('Kilometers Driven', 1000, 100000, step=5000)


encoding_dict= {

    "fuel": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric':5},
    "transmission": {"Manual":1, "Automatic":2}

}

def model_pred (fuel, transmission, engine, seats, make, km ):
    with open ("car_pred_model", "rb") as file:
        model=pickle.load(file)

    input_values=[[make, 1 , km , fuel , transmission, 18, engine, 100, seats]]

    return model.predict(input_values)


if st.button('Predict Car Price'):
    fuel = encoding_dict['fuel'][fuel]
    transmission=encoding_dict['transmission'][transmission]
    price= model_pred(fuel, transmission, engine, seats, make, km)

    st.text(f"Predicted price is: {np.round(float(np.array2string(price).strip('[]')),1)} lakhs")
