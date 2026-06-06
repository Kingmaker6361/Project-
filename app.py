import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="NG-E Shield", layout="wide")

st.title("NG-E Shield")
st.subheader("AI-Based Threat Classification & Prediction Prototype")

# Simulated Inputs
speed = st.slider("Speed (m/s)", 50, 3000, 800)
altitude = st.slider("Altitude (m)", 100, 30000, 12000)
signal_strength = st.slider("Signal Strength", 0, 100, 70)

# Classification Logic
if speed < 250:
    classification = "Drone"
elif speed < 600:
    classification = "UAV"
elif speed < 1200:
    classification = "Cruise-Type Threat"
elif speed < 2500:
    classification = "Ballistic-Type Threat"
else:
    classification = "Hypersonic-Type Threat"

confidence = np.random.randint(85, 99)

# Threat Level
if speed > 2000:
    threat_level = "HIGH"
elif speed > 800:
    threat_level = "MEDIUM"
else:
    threat_level = "LOW"

# Simulated Prediction
impact_zone = f"Zone-{np.random.randint(1,10)}"
time_to_impact = np.random.randint(60, 300)

# Threat Report
st.subheader("Threat Assessment Report")

report = {
    "Classification": classification,
    "Confidence": f"{confidence}%",
    "Threat Level": threat_level,
    "Predicted Impact Area": impact_zone,
    "Time To Impact": f"{time_to_impact} sec",
    "Tracking Stability": np.random.choice(
        ["High", "Medium", "Low"]
    ),
}

st.table(pd.DataFrame(report.items(), columns=["Field", "Value"]))

# Response Simulation (Research Only)
st.subheader("Response Simulation Results")

response_df = pd.DataFrame({
    "Scenario": ["Alpha", "Beta", "Gamma"],
    "Effectiveness Score": [
        np.random.randint(60,95),
        np.random.randint(40,85),
        np.random.randint(20,75)
    ]
})

st.dataframe(response_df, use_container_width=True)

best = response_df.loc[
    response_df["Effectiveness Score"].idxmax()
]

st.success(
    f"Highest Simulated Effectiveness: "
    f"{best['Scenario']} ({best['Effectiveness Score']}%)"
)
