import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="NG-E Shield",
    layout="wide"
)

st.title("🛡️ NG-E Shield")
st.subheader("AI-Based Aerial Object Analytics Prototype")

# ----------------------------------
# SIDEBAR INPUTS
# ----------------------------------

st.sidebar.header("Object Parameters")

speed = st.sidebar.slider(
    "Speed",
    0,
    1500,
    500
)

altitude = st.sidebar.slider(
    "Altitude",
    0,
    10000,
    3000
)

signal_strength = st.sidebar.slider(
    "Signal Strength",
    0,
    100,
    70
)

lat = st.sidebar.number_input(
    "Latitude",
    value=12.97,
    format="%.4f"
)

lon = st.sidebar.number_input(
    "Longitude",
    value=77.59,
    format="%.4f"
)

# ----------------------------------
# CLASSIFICATION
# ----------------------------------

if speed < 250:
    obj_type = "Drone"
    signal_type = "GNSS Signature"

elif speed < 600:
    obj_type = "UAV"
    signal_type = "RF Signature"

elif speed < 900:
    obj_type = "Aircraft"
    signal_type = "Aviation Signal"

elif speed < 1200:
    obj_type = "Cruise-Type Threat"
    signal_type = "Guidance Signal"

else:
    obj_type = "Ballistic-Type Threat"
    signal_type = "High Energy Signature"

confidence = np.random.randint(85, 99)

# ----------------------------------
# THREAT LEVEL
# ----------------------------------

if speed > 1000:
    threat_level = "HIGH"
elif speed > 500:
    threat_level = "MEDIUM"
else:
    threat_level = "LOW"

# ----------------------------------
# METRICS
# ----------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Object Type",
    obj_type
)

c2.metric(
    "Confidence",
    f"{confidence}%"
)

c3.metric(
    "Signal Category",
    signal_type
)

c4.metric(
    "Threat Level",
    threat_level
)

st.divider()

# ----------------------------------
# MAP
# ----------------------------------

st.subheader("Live Tracking Map")

pred_lat = lat + np.random.uniform(0.2, 0.8)
pred_lon = lon + np.random.uniform(0.2, 0.8)

m = folium.Map(
    location=[lat, lon],
    zoom_start=7
)

# current object
folium.Marker(
    [lat, lon],
    popup=f"{obj_type}",
    tooltip="Tracked Object"
).add_to(m)

# predicted location
folium.Marker(
    [pred_lat, pred_lon],
    popup="Predicted Position",
    icon=folium.Icon(color="red")
).add_to(m)

# path
folium.PolyLine(
    [
        [lat, lon],
        [pred_lat, pred_lon]
    ],
    weight=3
).add_to(m)

# multiple objects simulation
for i in range(10):

    sim_lat = lat + np.random.uniform(-1.0, 1.0)
    sim_lon = lon + np.random.uniform(-1.0, 1.0)

    folium.Marker(
        [sim_lat, sim_lon],
        popup=f"Object-{i+1}"
    ).add_to(m)

st_folium(
    m,
    width=1200,
    height=500
)

# ----------------------------------
# THREAT REPORT
# ----------------------------------

st.subheader("Threat Assessment Report")

impact_zone = f"Zone-{np.random.randint(1,10)}"

report = pd.DataFrame({
    "Parameter":[
        "Classification",
        "Confidence",
        "Speed",
        "Altitude",
        "Threat Level",
        "Predicted Impact Area"
    ],
    "Value":[
        obj_type,
        f"{confidence}%",
        speed,
        altitude,
        threat_level,
        impact_zone
    ]
})

st.dataframe(
    report,
    use_container_width=True
)

# ----------------------------------
# THREAT RANKING
# ----------------------------------

st.subheader("Threat Ranking")

threats = []

for i in range(10):

    score = np.random.randint(20,100)

    threats.append(
        [
            f"OBJ-{i+1}",
            score
        ]
    )

ranking = pd.DataFrame(
    threats,
    columns=[
        "Object ID",
        "Threat Score"
    ]
)

ranking = ranking.sort_values(
    by="Threat Score",
    ascending=False
)

st.dataframe(
    ranking,
    use_container_width=True
)

# ----------------------------------
# RESPONSE SIMULATION
# ----------------------------------

st.subheader("Response Simulation Results")

sim = pd.DataFrame({
    "Scenario":[
        "Alpha",
        "Beta",
        "Gamma"
    ],
    "Score":[
        np.random.randint(60,95),
        np.random.randint(40,85),
        np.random.randint(20,75)
    ]
})

st.dataframe(
    sim,
    use_container_width=True
)

# ----------------------------------
# CHART
# ----------------------------------

st.subheader("Threat Metrics")

chart = pd.DataFrame({
    "Metric":[
        "Speed",
        "Altitude",
        "Signal"
    ],
    "Value":[
        speed,
        altitude/100,
        signal_strength
    ]
})

st.bar_chart(
    chart.set_index("Metric")
)
