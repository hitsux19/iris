import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
import pickle

# Load the model 
with open('house_xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

def app():
    def location_map(lat, long):
        m = folium.Map(location=[lat, long], zoom_start=10)

        tooltip = "Potential House Location"
        folium.Marker(
            [lat, long], popup="Housing", tooltip=tooltip
        ).add_to(m)

        folium_static(m)

    st.title("California Housing Prediction App")


    st.sidebar.header("Input Features")
    housing_median_age = st.sidebar.slider('Average age of house (years)', 1.0, 52.0, 30.0)
    median_income = st.sidebar.slider('Median income (in millions)', 0.49, 8.06, 3.64, step=0.1)
    population = st.sidebar.slider('Population in the vicinity (thousands)', 3.00, 3117.00, 1188.00)
    households = st.sidebar.slider('Number of households (household)', 2, 1090, 417, step=10)
    total_rooms = st.sidebar.slider('Total room area (sqft)', 2, 5684, 2153, step=10)
    total_bedrooms = st.sidebar.slider('Total bedroom area (sqft)', 2, 1173, 445, step=10)
    lat = st.sidebar.number_input("Latitude", 32.5121, 41.95, 35.67, step=0.1)
    long = st.sidebar.number_input("Longitude", -124.6509, -114.1315, -119.59, step=0.05)

    if st.button('Estimate Price'):
        # Prepare input features (assuming your model expects these features in this order)
        input_features = np.array([housing_median_age, lat, long, total_rooms, total_bedrooms, population, households, median_income]).reshape(1, -1)

        # Make prediction
        with st.spinner("Calculating..."):
            predicted_price = model.predict(input_features)  # Use model.predict 

        st.success(f"Estimated House Price: ${predicted_price[0]:,.2f}")

    # Display the map
    location_map(lat, long)

app() 

