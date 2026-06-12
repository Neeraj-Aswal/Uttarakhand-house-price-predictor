# 🏠 Uttarakhand House Price Prediction System

## Overview

This project is a Machine Learning-based web application that predicts house prices across major cities in Uttarakhand.

The model uses property features such as city, area, BHK, bathrooms, property age, furnishing status, parking availability, and distance from the city center to estimate house prices.

## Features

* House price prediction
* Price range estimation
* Property category classification
* Interactive Streamlit interface
* Machine Learning powered predictions

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

## Machine Learning Model

* Algorithm: Random Forest Regressor
* Data Preprocessing: One-Hot Encoding
* R² Score: 94.13%
* Mean Absolute Error (MAE): 14.28 Lakh

## Input Parameters

* City
* Area (sq ft)
* BHK
* Bathrooms
* Property Age
* Parking Availability
* Furnishing Status
* Distance from City Center

## Project Structure

```text
app.py
house_model.pkl
model_columns.pkl
requirements.txt
README.md
```

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author

Neeraj Aswal
