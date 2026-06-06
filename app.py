import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="NG-E Shield",
    layout="wide"
)

st.title("🛡️ NG-E Shield")
st.subheader("AI-Based Threat Detection & Prediction Dashboard")

st.sidebar.header("Threat Input Parameters")

speed = st.sidebar.slider(
    "Speed (m/s)",
    100,
    3000,
    850
)

altitude = st.sidebar.slider(
    "Altitude (m)",
    100,
    30000,
    12000
)

signal_strength = st.sidebar.slider(
    "Signal Strength",
    0,
    100,
    70
)

# Classification

if speed < 300:
    classification = "Drone"

elif speed < 700:
    classification = "UAV"

elif speed < 1200:
    classification = "Cruise-Type Threat"

elif speed < 2500:
    classification = "Ballistic-Type Threat"

else:
    classification = "Hypersonic-Type Threat"

confidence = np.random.randint(85, 99)

# Threat level

if speed > 2000:
    threat_level = "HIGH"

elif speed > 1000:
    threat_level = "MEDIUM"

else:
    threat_level = "LOW"

impact_zone = f"Zone-{np.random.randint(1,10)}"

time_to_impact = np.random.randint(60, 300)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Classification",
        classification
    )

with col2:
    st.metric(
        "Confidence",
        f"{confidence}%"
    )

with col3:
    st.metric(
        "Threat Level",
        threat_level
    )

st.markdown("---")

st.subheader("Threat Assessment Report")

report = {
    "Classification": classification,
    "Confidence": f"{confidence}%",
    "Altitude": altitude,
    "Speed": speed,
    "Impact Zone": impact_zone,
    "Time To Impact": f"{time_to_impact} sec",
    "Threat Level": threat_level
}

st.table(
    pd.DataFrame(
        report.items(),
        columns=["Parameter", "Value"]
    )
)

st.subheader("Response Simulation")

scenario_df = pd.DataFrame({
    "Scenario": [
        "Alpha",
        "Beta",
        "Gamma"
    ],
    "Score": [
        np.random.randint(60,95),
        np.random.randint(40,85),
        np.random.randint(20,75)
    ]
})

st.dataframe(
    scenario_df,
    use_container_width=True
)

st.subheader("Threat Score Chart")

chart_data = pd.DataFrame({
    "Threat Metric": [
        "Speed",
        "Altitude",
        "Signal"
    ],
    "Value": [
        speed,
        altitude/100,
        signal_strength
    ]
})

st.bar_chart(
    chart_data.set_index(
        "Threat Metric"
    )
)
