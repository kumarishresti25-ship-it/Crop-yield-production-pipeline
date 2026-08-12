#  Agricultural Risk & Yield Analytics Platform

An interactive geospatial analytics platform designed to monitor crop health, evaluate drought risks, and forecast agricultural productivity using satellite imagery and weather time-series data.

![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Scikit-Learn](https://img.shields.io/badge/ML-Random%20Forest-green.svg)

---

# Key Features

 Vegetation Index Tracking (NDVI/EVI): Computes and visualizes normalized difference vegetation indices over time to monitor plant health and growth cycles.
 Drought Risk Probability Scoring: Evaluates environmental factors to provide real-time drought probability metrics across major farming regions.
 Yield Forecasting & Confidence Intervals: Predicts crop yields (tons/hectare) alongside statistical confidence bounds using feature-engineered regression models.
 Multi-Region Coverage: Built-in support for analyzing specific agricultural belts and zones across India (including Punjab, Bihar, Jharkhand, Chhattisgarh, Maharashtra, and more).

---

# Tech Stack
Frontend & Dashboard: Streamlit
Machine Learning & Analytics: Scikit-Learn (Random Forest Regressor), NumPy, Pandas
Geospatial Processing: Rasterio, Earthpy
Data Visualization: Matplotlib

---

# Project Structure

Crop-Yield-Prediction-Pipeline/
│
├── app.py                  # Main Streamlit dashboard interface
├── model.py                # Machine learning model definition & training logic
├── data_processor.py       # Geospatial data processing & index computation
├── requirements.txt        # Project dependencies
└── .gitignore              # Git ignore file
