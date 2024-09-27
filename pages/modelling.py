import streamlit as st

def app():
    st.title("Model Selection and Performance")

    st.write("""
    ## Building Machine Learning Models for Regression

    The goal is to predict house prices (our target variable) based on features like house size and location.  Here's how we built and evaluated our models:

    **1. Data Preparation:**

    * **Loading:**  We started by importing the California Housing dataset.
    * **Exploration (EDA):** We analyzed the data to understand its patterns and identify potential outliers.
    * **Handling Outliers:** Outliers are extreme values that can skew our models. We used visualization and statistical methods to identify and handle them.
    * **Feature Engineering:**  We explored creating new features from existing ones to potentially improve model accuracy. 

    **2. Train-Test Split:**

    * We split the data into a **training set** (used to train the models) and a **testing set** (used to evaluate the models on unseen data).
    * This split helps us assess how well our models generalize to new data.

    **3. Model Selection and Training:**

    We experimented with several regression models:

    * **Linear Regression:** Assumes a linear relationship between features and the target variable.
    * **Decision Tree:** Creates a tree-like structure to make predictions based on feature values.
    * **Random Forest:** Combines multiple decision trees for better generalization.
    * **XGBoost:** A powerful gradient boosting algorithm known for its performance. 
    * **Support Vector Machine (SVM):**  Finds the best boundary to separate data points (can be adapted for regression).
    * **Neural Network (NN/MLP):**  Models complex relationships using interconnected nodes.

    **4. Model Evaluation (Mean Squared Error - MSE):**

    We used Mean Squared Error (MSE) to measure how well our models predict house prices. Lower MSE means better accuracy.

    ## Results:

    | Model                 | MSE                  |
    |----------------------|----------------------|
    | Linear Regression   | 5,566,031,385.98     |
    | Decision Tree       | 5,263,094,533.71     |
    | Random Forest       | 2,766,754,240.08     |
    | **XGBoost**         | **2,618,908,282.43** | 
    | SVM                 | 43,591,759,567.40    |
    | NN/MLP              | 10,987,891,712.00    |

    ## Analysis:

    * **Best Model:** XGBoost achieved the lowest MSE, indicating the most accurate predictions on this dataset.
    * **Other Good Performers:**  Random Forest also demonstrated strong performance.
    * **Models To Improve:** The higher MSE values for Linear Regression, Decision Tree, SVM, and NN/MLP suggest they might need further refinement or may not be the best fit for this data.

    ## Important Considerations:

    * **Data Preprocessing (Outliers, Feature Engineering):**  Cleaning and preparing the data significantly impacts model accuracy.
    * **Hyperparameter Tuning:** Each model has settings that can be adjusted for optimal performance.
    * **Overfitting:**  A model might perform well on training data but poorly on new data (overfitting).
    * **Choosing the Right Model:** The "best" model depends on the specific dataset, desired accuracy, interpretability, and computational costs.
    """)
app() 