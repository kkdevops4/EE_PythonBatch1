import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk
from datetime import datetime, timedelta
import requests

@st.cache_data
def get_osrm_route(start_lat, start_lon, end_lat, end_lon):

    url = (
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{start_lon},{start_lat};{end_lon},{end_lat}"
        f"?overview=full&geometries=geojson"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        if not data.get("routes"):
            return None

        return data["routes"][0]["geometry"]["coordinates"]

    except Exception:
        return None

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Vehicle Telematics",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Vehicle Route Analytics Dashboard (High-Speed Alert System)")


# -----------------------------
# FIXED ROUTE (INPUT REMOVED)
# -----------------------------

start_lat = 18.5204
start_lon = 73.8567

end_lat = 18.6298
end_lon = 73.7997


# -----------------------------
# ROUTE GENERATION (0–180 KM/H)
# -----------------------------
@st.cache_data
def generate_route(start_lat, start_lon, end_lat, end_lon):

    steps = 120
    base_time = datetime.now()

    data = []

    for i in range(steps):

        t = i / (steps - 1)

        lat = start_lat + (end_lat - start_lat) * t
        lon = start_lon + (end_lon - start_lon) * t

        # -----------------------------
        # SPEED MODEL (UP TO 180)
        # -----------------------------
        base_speed = 60 + 90 * np.sin(t * np.pi)
        noise = np.random.randn() * 10

        spike = np.random.choice(
            [0, 15, -10, 20, -20, 35],
            p=[0.70, 0.08, 0.06, 0.07, 0.05, 0.04]
        )

        speed = base_speed + noise + spike

        # clamp 0–180
        speed = max(0, min(180, speed))

        data.append({
            "latitude": lat,
            "longitude": lon,
            "speed": speed,
            "timestamp": base_time + timedelta(seconds=i)
        })

    return pd.DataFrame(data)


df = generate_route(start_lat, start_lon, end_lat, end_lon)


# -----------------------------
# CLEANING
# -----------------------------
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")
df["time_display"] = df["timestamp"].dt.strftime("%M:%S.%f").str[:-3]


# -----------------------------
# SPEED FILTER
# -----------------------------
st.sidebar.subheader("🎚 Speed Filter")

min_speed = int(df["speed"].min())
max_speed = int(df["speed"].max())

speed_range = st.sidebar.slider(
    "Select Speed Range",
    min_value=min_speed,
    max_value=max_speed,
    value=(min_speed, max_speed)
)

df_filtered = df[
    (df["speed"] >= speed_range[0]) &
    (df["speed"] <= speed_range[1])
]

if df_filtered.empty:
    st.warning("No data in selected speed range.")
    st.stop()


# -----------------------------
# 🚨 SPEED ALERT SYSTEM
# -----------------------------
high_speed_df = df_filtered[df_filtered["speed"] > 120]

if not high_speed_df.empty:
    st.error(f"🚨 ALERT: {len(high_speed_df)} overspeeding events detected (>120 km/h)")
    st.warning("High-speed driving detected. Review highlighted rows below.")


# -----------------------------
# KPIs
# -----------------------------
st.subheader("📊 Route KPIs (Filtered)")

c1, c2, c3 = st.columns(3)

c1.metric("Max Speed", f"{df_filtered['speed'].max():.1f} km/h")
c2.metric("Avg Speed", f"{df_filtered['speed'].mean():.1f} km/h")
c3.metric("Min Speed", f"{df_filtered['speed'].min():.1f} km/h")


# -----------------------------
# MAP (REAL ROAD ROUTE USING OSRM)
# -----------------------------
st.subheader("🗺 Route Visualization")

path = get_osrm_route(
    start_lat,
    start_lon,
    end_lat,
    end_lon
)

if path:

    route_layer = pdk.Layer(
        "PathLayer",
        data=[{"path": path}],
        get_path="path",
        get_color=[0, 255, 180],
        width_scale=20,
        width_min_pixels=6
    )

    start_layer = pdk.Layer(
        "ScatterplotLayer",
        data=[{
            "lat": start_lat,
            "lon": start_lon
        }],
        get_position="[lon, lat]",
        get_fill_color=[0, 255, 0],
        get_radius=120
    )

    end_layer = pdk.Layer(
        "ScatterplotLayer",
        data=[{
            "lat": end_lat,
            "lon": end_lon
        }],
        get_position="[lon, lat]",
        get_fill_color=[255, 0, 0],
        get_radius=120
    )

    vehicle_layer = pdk.Layer(
        "ScatterplotLayer",
        data=[{
            "lat": df.iloc[-1]["latitude"],
            "lon": df.iloc[-1]["longitude"]
        }],
        get_position="[lon, lat]",
        get_fill_color=[255, 255, 0],
        get_radius=100
    )

    deck = pdk.Deck(
        map_style="road",
        initial_view_state=pdk.ViewState(
            latitude=(start_lat + end_lat) / 2,
            longitude=(start_lon + end_lon) / 2,
            zoom=11,
            pitch=45
        ),
        layers=[
            route_layer,
            start_layer,
            end_layer,
            vehicle_layer
        ],
        tooltip={
            "text": "Vehicle Route"
        }
    )

    st.pydeck_chart(deck)

else:
    st.error("Unable to fetch route from OSRM.")

# -----------------------------
# SPEED TREND
# -----------------------------
st.subheader("📈 Speed Trend (Real Driving Behavior)")

fig_line = px.line(
    df_filtered,
    x="time_display",
    y="speed",
    markers=True,
    title="Speed vs Time"
)

fig_line.update_traces(
    line_color="#000000",
    line_width=2
)

fig_line.update_layout(template="plotly_dark")

st.plotly_chart(fig_line, use_container_width=True)


# -----------------------------
# ROUTE DETAILS
# -----------------------------
st.subheader("📍 Route Details")

col1, col2 = st.columns(2)

col1.info(f"""
🏠 START  
Latitude: {start_lat}  
Longitude: {start_lon}
""")

col2.success(f"""
🏢 END  
Latitude: {end_lat}  
Longitude: {end_lon}
""")

# -----------------------------
# TABLE (WITH RISK FLAG)
# -----------------------------
def highlight_speed(row):
    return ['background-color: red' if row.speed > 120 else '' for _ in row]

st.subheader("📋 Filtered Route Data (Risk Highlighted)")

st.dataframe(df_filtered.style.apply(highlight_speed, axis=1))