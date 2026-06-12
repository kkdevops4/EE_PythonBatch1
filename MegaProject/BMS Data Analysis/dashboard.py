# =====================================================
# INSTRUCTIONS 
# =====================================================
'''
Run with:
    python -m streamlit run dashboard.py
'''

# =====================================================
# IMPORTING 
# =====================================================
import streamlit as st
import pandas as pd
import plotly.express as px

from analytics import *

import plotly.graph_objects as go

# =====================================================
# SETTING PAGE CONFIGURATION 
# =====================================================
st.set_page_config(
    page_title="EV Battery Analysis",
    page_icon="⚡",
    layout="wide"
)

# =====================================================
# LOAD DATA 
# =====================================================
df = load_data("processed_data/processed_battery_data.xlsx")

# =====================================================
# TITLE 
# =====================================================
st.title("BATTERY MANAGEMENT SYSTEM")
st.caption("EV Battery Analytics Dashboard")

# =====================================================
# KPI STRIP 
# =====================================================
soc = soc_summary(df)
soh = soh_summary(df)
temp = temperature_summary(df)

latest_soc = soc["Latest SoC"]
latest_soh = soh["Latest SoH"]
latest_voltage = round(df["battery_voltage_v"].iloc[-1], 2)
peak_temp = temp["Maximum Temperature"]
avg_temp = temp["Average Temperature"]

charging_rows = (df["state"] == "Charging").sum()
charging_hours = round((charging_rows*10)/3600, 2)

st.subheader("Battery Overview")

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Latest SoC", f"{latest_soc}%")
col2.metric("Latest SoH", f"{latest_soh}%")
col3.metric("Latest Voltage", f"{latest_voltage} V")
col4.metric("Peak Temperature", f"{peak_temp} °C")
col5.metric("Charging Time", f"{charging_hours} hrs")
col6.metric("Average Temperature", f"{avg_temp} °C")

st.divider()

# =====================================================
# STATE OF CHARGE  
# =====================================================
st.subheader("State of Charge Trend")

fig = px.line(
    df,
    x = "timestamp",
    y = "soc_percent",
    title = "State of Charge Over Time"
)
fig.update_xaxes(showgrid = True)
fig.update_yaxes(showgrid = True)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info("""
Upward slope = Charging
        
Downward slope = Driving / Battery Usage
        
Flat line = Idle / Minimal Battery Activity
""")

st.divider()

# =====================================================
# VOLTAGE AND CURRENT TRENDS 
# =====================================================
st.subheader("Battery Voltage and Current Trends")

fig = px.line(
    df,
    x = "timestamp",
    y = "battery_voltage_v",
    title = "Battery Voltage over time"
)
fig.update_xaxes(showgrid = True)
fig.update_yaxes(showgrid = True)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.caption(
    "Voltage may rise during charging and drop under heavy load."
)

fig = px.line(
    df,
    x = "timestamp",
    y = "battery_current_a", 
    title = "Battery current over time" 
)
fig.update_xaxes(showgrid = True)
fig.update_yaxes(showgrid = True)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info("""
Positive Current = Battery Discharging while Driving

Negative Current = Battery Charging

Current Near Zero = Idle State
""")

st.divider()

# =====================================================
# TEMPERATURE TRENDS 
# =====================================================
st.subheader("Battery Temperature Trends")

fig = px.line(
    df,
    x = "timestamp",
    y = "battery_temp_c",
    title = "Battery Temperature Over Time"
)
fig.update_xaxes(showgrid = True)
fig.update_yaxes(showgrid = True)
fig.add_hline(
    y = 45,
    line_dash = "dash",
    annotation_text = "Warning Threshold (45°C)"
)

st.plotly_chart(
    fig,
     use_container_width=True
)

max_temp = temp["Maximum Temperature"]
min_temp = temp["Minimum Temperature"]

# col1, col2 = st.columns(2)

# col1.metric("Maximum Temperature", f"{max_temp} °C")
# col2.metric("Minimum Temperature", f"{min_temp} °C")

st.info(f"Maximum Temperature, {max_temp} °C")
st.info(f"Minimum Temperature, {min_temp} °C")

if df["battery_temp_c"].max() > 45:
    st.error("Temperature exceeded the warning threshold")
else:
    st.success("Temperature within safe limits.")

st.caption("Higher temperatures may indicate heavy vehicle usage, fast charging, or cooling system inefficiencies.")

st.divider()

# =====================================================
# BATTERY SUMMARY 
# =====================================================

min_soc = soc["Minimum SoC"]
max_soc = soc["Maximum SoC"]
latest_soh = soh["Latest SoH"]
max_temp = temp["Maximum Temperature"]

# =====================================================
if max_temp > 45:
    temp_status = "Warning"
else:
    temp_status = "safe"
# =====================================================
if max_temp > 45:
    overall_status = "Attention Required"
else:
    overall_status = "Normal Operation"
# =====================================================
if latest_soh >= 95:
    health_status = "Excellent"
elif latest_soh >= 90:
    health_status = "Good"
elif latest_soh >= 80:
    health_status = "Moderate Degradation"
else:
    health_status = "Attention Required"
# =====================================================
if latest_soh < 80 or max_temp > 45:
    overall_status = "Attention Required"
elif latest_soh < 90:
    overall_status = "Monitor Battery Condition"
else:
    overall_status = "Normal Operation"
# =====================================================
st.markdown(f"""
### Battery Health Summary

- Battery health remained at **{latest_soh}% SoH**.

- Health Status: **{health_status}**

- State of charge ranged between **{min_soc}%** and **{max_soc}%**.

- Total charging duration was approximately **{charging_hours} hours**.

- Maximum battery temperature reached **{max_temp}°C**.

- Temperature Status: **{temp_status}**

- Overall Battery Condition: **{overall_status}**
""")