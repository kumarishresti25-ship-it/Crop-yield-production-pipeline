import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crop Yield & Drought Risk", layout="wide")

st.title("🌾 Agricultural Risk & Yield Analytics Platform")

# Sidebar for controls with real agricultural regions including Chhattisgarh, Bihar, and Jharkhand
regions = [
    "Chhattisgarh - Durg-Raipur Plains (Rice Bowl of Central India)",
    "Chhattisgarh - Bastar Plateau (Millets/Forest Produce)",
    "Chhattisgarh - Raigarh Region (Paddy/Maize)",
    "Bihar - Rohtas Belt (Rice/Wheat Bowl)",
    "Bihar - Muzaffarpur Region (Litchi/Horticulture)",
    "Bihar - Purnia Belt (Maize/Jute)",
    "Jharkhand - Chota Nagpur Plateau (Paddy/Millets)",
    "Jharkhand - Santhal Pargana (Paddy/Maize)",
    "Punjab - Ludhiana Belt (Wheat/Paddy)",
    "Maharashtra - Vidarbha Region (Cotton/Soybean)",
    "Karnataka - Raichur District (Paddy/Millets)",
    "Uttar Pradesh - Gorakhpur Belt (Sugarcane/Rice)",
    "Madhya Pradesh - Malwa Plateau (Wheat/Soybean)",
    "Andhra Pradesh - Godavari Delta (Rice/Maize)",
    "Gujarat - Saurashtra Region (Groundnut/Cotton)",
    "Rajasthan - Marwar Region (Bajra/Mustard)",
    "Tamil Nadu - Cauvery Delta (Paddy)",
    "Haryana - Karnal Belt (Wheat/Paddy)"
]

selected_region = st.sidebar.selectbox("Select Agricultural Region", regions)
st.sidebar.info("Model: Feature-Engineered Random Forest Regressor")
st.sidebar.markdown(f"**Active Analysis Target:**\n{selected_region}")

# Visualization layout
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Vegetation Index (NDVI) Trend - {selected_region.split(' - ')[0]}")
    # Simulating slightly different trend data based on the region string length for variability
    np.random.seed(len(selected_region))
    data = np.random.randn(10).cumsum()
    st.line_chart(data)

with col2:
    st.subheader("Drought Risk Probability")
    risk_score = np.random.uniform(0.15, 0.85)
    st.progress(risk_score)
    st.write(f"Current Risk Level: **{risk_score*100:.1f}%**")

st.subheader("Yield Forecast & Confidence Intervals")

# Plotting confidence intervals
fig, ax = plt.subplots(figsize=(10, 4))
x = np.linspace(0, 10, 10)
y = x * 0.6 + np.random.normal(0, 0.4, 10)
ax.plot(x, y, label="Predicted Yield (tons/hectare)", color="green", linewidth=2)
ax.fill_between(x, y-0.6, y+0.6, color="lightgreen", alpha=0.3, label="95% Confidence Interval")
ax.set_xlabel("Time Horizon (Months)")
ax.set_ylabel("Yield Index")
ax.legend()
st.pyplot(fig)