import streamlit as st
from PIL import Image  # Import Image

def app():
    
   st.title("SHAP Value Analysis for California Housing Prices")

   st.header("Feature Importance (SHAP Summary Plot)")
   image_summary = Image.open('shap_calhouse.png')  
   st.image(image_summary, use_column_width=True)


   st.write("""
   This SHAP (SHapley Additive exPlanations) plot illustrates the impact of each feature on the model's prediction 
   for median house prices in a given California location during the 1990s. 
   Below is a breakdown of the SHAP value results:
   """)

   st.subheader("Feature Impact:")

   st.markdown("""
   1. **Latitude:**
      - Red color indicates high feature values (further north).
      - Blue color indicates low feature values (further south).
      - SHAP values suggest that higher latitude (further north) tends to lower house prices, 
        while lower latitude (further south) tends to increase them.
  
   2. **Longitude:**
      - Red color indicates high feature values (further east).
      - Blue color indicates low feature values (further west).
      - SHAP values suggest that higher longitude (further east) tends to lower house prices, 
        while lower longitude (further west) tends to increase them.

   3. **Median Income:**
      - Red color indicates high feature values (higher income).
      - Blue color indicates low feature values (lower income).
      - SHAP values strongly indicate that higher median income significantly increases house prices, 
        while lower median income decreases them.

   4. **Total Rooms:**
      - Red color indicates high feature values (more rooms).
      - Blue color indicates low feature values (fewer rooms).
      - Total rooms show a mixed impact but generally suggest that more rooms slightly increase house prices.

   5. **Population:**
      - Red color indicates high feature values (higher population).
      - Blue color indicates low feature values (lower population).
      - SHAP values suggest that higher population tends to lower house prices, 
        while lower population tends to increase them.

   6. **Housing Median Age:**
      - Red color indicates high feature values (older houses).
      - Blue color indicates low feature values (newer houses).
      - SHAP values suggest that older houses tend to lower house prices, 
        while newer houses tend to increase them.

   7. **Total Bedrooms:**
      - Red color indicates high feature values (more bedrooms).
      - Blue color indicates low feature values (fewer bedrooms).
      - Total bedrooms have a less pronounced impact but suggest that more bedrooms slightly increase house prices.

   8. **Households:**
      - Red color indicates high feature values (more households).
      - Blue color indicates low feature values (fewer households).
      - SHAP values suggest that a higher number of households tends to lower house prices, 
        while a lower number tends to increase them.
   """)

   st.subheader("Conclusion:")

   st.write("""
   Overall, median income is the most significant feature influencing median house prices, 
   followed by geographical location (latitude and longitude). Other features like total rooms, 
   population, housing median age, total bedrooms, and households also have an impact, 
   but not as substantial as median income and location.
   """)
app() 

