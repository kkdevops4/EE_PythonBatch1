'''
Run with:
    python -m streamlit run dashboard.py
'''

import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


st.set_page_config(layout="wide") #make Streamlit wider

# st.title("EV BMS Data Analysis")
st.markdown(
    """
<h1 style = 'text-align: center; color: gray;'>
Battery Management System 
</h1>

<h4 style = 'text-align: center; color: gray;'>
Battery Analytics System
</h4>
""",
unsafe_allow_html=True
)


# =====================================================
# READ DATA 
# =====================================================
df = pd.read_excel("processed_data/processed_battery_data.xlsx")
ideal_df = pd.read_csv("data/ideal_BMWi3_battery_dataset_24h.csv")

#VEHICLE DETAILS
st.subheader("Vehicle Information")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Vehicle", "BMW i3")
    st.metric("Battery Capacity", "22 kWh")
with col2:
    st.metric("Battery Rating", "60 Ah")
    st.metric("Battery Type", "Li-Ion")
# with col3:
#     st.metric("Owner Name:", "Name")
st.markdown("---")

# =====================================================
# SUMMARY & INSIGHTS
# =====================================================
# st.subheader("LATEST READINGS")
from analytics import *

df = load_data("processed_data/processed_battery_data.xlsx")

soc = soc_summary(df)
soh = soh_summary(df)
temp = temperature_summary(df)
power = power_summary(df)

# # =====================================================
# # SOC INSIGHTS
# # =====================================================
# st.subheader("SoC Insights")

# col1, col2, col3, col4 = st.columns(4)

# col1.metric("Latest SOC", soc["Latest Soc"])
# col2.metric("Average SOC", soc["Average Soc"])
# col3.metric("Minimum SOC", soc["Minimum SoC"])
# col4.metric("Maximum SOC", soc["Maximum SoC"])

# # =====================================================
# # SOH INSIGHTS
# # =====================================================
# st.subheader("SOH Insights")

# col1, col2, col3, col4 = st.columns(4)

# col1.metric("Latest SOH (%)", soh["Latest SoH"])
# col2.metric("Average SOH (%)", soh["Average SoH"])
# col3.metric("Minimum SOH (%)", soh["Minimum SoH"])
# col4.metric("Maximum SOH (%)", soh["Maximum SoH"])

# # =====================================================
# # TEMPERATURE INSIGHTS
# # =====================================================
# st.subheader("Temperature Insights")

# col1, col2, col3 = st.columns(3)

# col1.metric("Average Temp (°C)",temp["Average Temperature"])
# col2.metric("Minimum Temp (°C)",temp["Minimum Temperature"])
# col3.metric("Maximum Temp (°C)",temp["Maximum Temperature"])

# # =====================================================
# # POWER INSIGHTS
# # =====================================================
# st.subheader("Power Insights")

# col1, col2 = st.columns(2)

# col1.metric("Average Power (kW)",power["Average Power"])
# col2.metric("Peak Power (kW)",power["Maximum Power"])

st.subheader("BATTERY STATISTICS")
# =====================================================
# SOC INSIGHTS
# =====================================================
with st.expander("State of Charge Statistics", expanded=True):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Latest SOC (%)", soc["Latest Soc"])
    col2.metric("Average SOC (%)", soc["Average Soc"])
    col3.metric("Minimum SOC (%)", soc["Minimum SoC"])
    col4.metric("Maximum SOC (%)", soc["Maximum SoC"])


# =====================================================
# SOH INSIGHTS
# =====================================================
with st.expander("State of Health Statistics", expanded=True):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Latest SOH (%)", soh["Latest SoH"])
    col2.metric("Average SOH (%)", soh["Average SoH"])
    col3.metric("Minimum SOH (%)", soh["Minimum SoH"])
    col4.metric("Maximum SOH (%)", soh["Maximum SoH"])


# =====================================================
# TEMPERATURE INSIGHTS
# =====================================================
with st.expander("Temperature Statistics", expanded=True):

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Temp (°C)",temp["Average Temperature"])
    col2.metric("Minimum Temp (°C)",temp["Minimum Temperature"])
    col3.metric("Maximum Temp (°C)",temp["Maximum Temperature"])


# =====================================================
# POWER INSIGHTS
# =====================================================
with st.expander("Power Statistics", expanded=True):

    col1, col2 = st.columns(2)

    col1.metric("Average Power (kW)",power["Average Power"])
    col2.metric("Peak Power (kW)",power["Maximum Power"])

st.divider()


# analytics = generate_analytics(df)
# #KPI CARDS
# health = analytics["battery_health"]
# soc = analytics["soc"]
# temp = analytics["temperature"]
# power = analytics["power"]

# col1,col2,col3,col4 = st.columns(4)

# col1.metric("Current SOC",f"{soc['Current SOC']}%")
# col2.metric("Current SOH",f"{health['Current SOH']}%")
# col3.metric("Avg Temp",f"{temp['Average Temp']} °C")
# col4.metric("Avg Power",f"{power['Average Power']} kW")
# st.markdown("---")

# =====================================================
# ALERT SYSTEM
# =====================================================
st.subheader("Battery Condition Monitor")
# Latest values
latest_temp = df["battery_temp_c"].iloc[-1]
latest_soc = df["soc_percent"].iloc[-1]
latest_soh = df["soh_percent"].iloc[-1]
# Temperature Status
def check_temperature(temp):
    if temp > 50:
        return "Critical"
    elif temp > 40:
        return "Warning"
    else:
        return "Normal"
status = check_temperature(latest_temp)
if status == "Critical":st.error(f"Temperature Status: CRITICAL ({latest_temp:.1f} °C)")
elif status == "Warning":st.warning(f"Temperature Status: WARNING ({latest_temp:.1f} °C)")
else:st.success(f"Temperature Status: NORMAL ({latest_temp:.1f} °C)")

# Alert Rules
alerts = []
if latest_temp > 40:
    alerts.append(f"High Battery Temperature: {latest_temp:.1f} °C")
if latest_soc < 20:
    alerts.append(f"Low State of Charge: {latest_soc:.1f}%")
if latest_soh < 80:
    alerts.append(f"Battery Health Warning: SOH = {latest_soh:.1f}%")

# Display Alerts
if alerts:
    st.subheader("Active Alerts")
    for alert in alerts:
        st.error(alert)
else:
    st.success(
        "No Active Alerts"
    )

st.divider()

# =====================================================
# SUMMARY VALUES
# =====================================================

soc_peak = df["soc_percent"].max()
soc_floor = df["soc_percent"].min()

voltage_peak = df["battery_voltage_v"].max()
voltage_floor = df["battery_voltage_v"].min()

temp_peak = df["battery_temp_c"].max()
temp_floor = df["battery_temp_c"].min()

current_peak = df["battery_current_a"].max()
current_floor = df["battery_current_a"].min()

# =====================================================
# 2x2 BATTERY PERFORMANCE CHARTS
# =====================================================
st.subheader("Battery Performace at a Glance")
fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "State of Charge (%)",
        "Battery Voltage (V)",
        "Battery Temperture (°C)",
        "Battery Current (A)"
    )
)

#SoC Graph
fig.add_trace(
    go.Scatter(
        x = df["timestamp"],
        y = df["soc_percent"],
        mode = "lines",
        name = "SoC"
    ),
    row=1,
    col=1
    )

fig.update_xaxes(title_text="Timestamp", row=1, col=1)
fig.update_yaxes(title_text="SOC (%)", row=1, col=1)

#ANNOTATE INISDE GRAPH
fig.add_annotation(
    text=f"Peak Value: {soc_peak:.1f}%<br>Seal Floor: {soc_floor:.1f}%",
    xref="x domain",
    yref="y domain",
    x=0.02,
    y=0.98,
    showarrow=False,
    row=1,
    col=1
)
##ADD DOTTED MAX AND MIN VALUE INSIDE CHART
# fig.add_hline(
#     y=soc_peak,
#     line_dash="dash",
#     annotation_text=f"Peak SOC: {soc_peak:.1f}%",
#     row=1,
#     col=1
# )
# fig.add_hline(
#     y=soc_floor,
#     line_dash="dot",
#     annotation_text=f"Floor SOC: {soc_floor:.1f}%",
#     row=1,
#     col=1
# )

#Voltage Graph
fig.add_trace(
    go.Scatter(
        x = df["timestamp"],
        y = df["battery_voltage_v"],
        mode = "lines",
        name = "Voltage"
    ),
    row=1,
    col=2
    )
fig.update_xaxes(title_text="Timestamp", row=1, col=2)
fig.update_yaxes(title_text="Voltage (V)", row=1, col=2)

#Temperature Graph
fig.add_trace(
    go.Scatter(
        x = df["timestamp"],
        y = df["battery_temp_c"],
        mode = "lines",
        name = "Tempertaure"
    ),
    row=2,
    col=1
    )
fig.update_xaxes(title_text="Timestamp", row=2, col=1)
fig.update_yaxes(title_text="Temperature (°C)", row=2, col=1)

#Current Graph
fig.add_trace(
    go.Scatter(
        x = df["timestamp"],
        y = df["battery_current_a"],
        mode = "lines",
        name = "Current"
    ),
    row=2,
    col=2
    ) 
fig.update_xaxes(title_text="Timestamp", row=2, col=2)
fig.update_yaxes(title_text="Current (A)", row=2, col=2)

#Format
fig.update_layout(
    template = "plotly_dark",
    height = 800,
    showlegend = False,
    title = "Battery Performance Trends "
)

st.plotly_chart(
    fig,
    use_container_width=True
)

#DESCRIPTION
col1, col2 = st.columns(2)

with col1:
    st.caption(f"SOC: Peak={soc_peak:.1f}% | Floor={soc_floor:.1f}%")

with col2:
    st.caption(f"Voltage: Peak={voltage_peak:.1f}V | Floor={voltage_floor:.1f}V")

col3, col4 = st.columns(2)

with col3:
    st.caption(f"Temp: Peak={temp_peak:.1f}°C | Floor={temp_floor:.1f}°C")

with col4:
    st.caption(f"Current: Peak={current_peak:.1f}A | Floor={current_floor:.1f}A")

st.divider()



# =====================================================
# BATTERY HEALTH
# =====================================================
st.subheader("BATTERY HEALTH")
fig = px.line(
    df,
    x="timestamp",
    y="soh_percent",
    title="Battery Health Trend"
)
fig.update_xaxes(title_text="Timestamp")
fig.update_yaxes(title_text="State of Health (%)")

st.plotly_chart(fig)

initial_soh = df["soh_percent"].iloc[0]
latest_soh = df["soh_percent"].iloc[-1]

soh_drop = initial_soh - latest_soh

st.info(
    f"Battery health decreased by {soh_drop:.2f}% during the monitored period, "
    f"from {initial_soh:.2f}% to {latest_soh:.2f}%."
)

st.divider()


# =====================================================
# SOC ANALYSIS
# =====================================================
st.subheader("SOC ANALYSIS")

# soc_trend = hourly_soc_trend(df)
# fig = px.line(
#     soc_trend,
#     x="hour",
#     y="soc_percent",
#     markers=True,
#     title="Hourly Average SOC"
# )

# st.plotly_chart(fig)

driving_df = df[df["state_refined"] == "Driving"]

soc_lost = (
    driving_df["soc_percent"].iloc[0] -
    driving_df["soc_percent"].iloc[-1]
)

st.metric("SOC Lost During Driving",f"{soc_lost:.2f}%")
st.markdown("---")

# # TEMPERATURE ANALYSIS
# st.subheader("TEMPERATURE ANALYSIS")

# temp_trend = hourly_temperature_trend(df)
# fig = px.line(
#     temp_trend,
#     x="hour",
#     y="battery_temp_c",
#     markers=True,
#     title="Hourly Average Temperature"
# )
# st.plotly_chart(fig, use_container_width=True)

# #SEVERITY
# severity = severity_analysis(df)
# fig = px.pie(
#     severity,
#     values="count",
#     names="severity",
#     hole=0.4
# )
# st.plotly_chart(fig, use_container_width=True)
# st.markdown("---")

# # CHARGING BEHAVIOUR
# st.subheader("CHARGING BEHAVIOUR")

# charging = charging_analysis(df)
# fig = px.pie(
#     charging,
#     values="count",
#     names="battery_status",
#     hole=0.4
# )
# st.plotly_chart(fig, use_container_width=True)

#TOTAL CHRAGING TIME
charging_rows = len(df[df["state"]=="Charging"])
charging_hours = (charging_rows * 10) / 3600
st.metric("Total Charging Time",f"{charging_hours:.2f} Hours")
st.markdown("---")

# ACTUAL VS IDEAL
st.subheader("ACTUAL VS IDEAL")
ideal_df = pd.read_csv(
    "data/ideal_BMWi3_battery_dataset_24h.csv"
)

ideal_df["timestamp"] = pd.to_datetime(ideal_df["timestamp"])

#SOC COMPARISION
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df["timestamp"],
        y=df["soc_percent"],
        name="Actual SoC"
    )
)
fig.add_trace(
    go.Scatter(
        x=ideal_df["timestamp"],
        y=ideal_df["soc_percent"],
        name="Ideal SoC"
    )
)
# fig.update_layout(
#     template = "plotly_dark",
#     height = 500,
#     showlegend = False,
#     title = "Actual SoC vs Ideal SoC"
# )
fig.update_layout(
    title = "Actual SoC vs Ideal SoC"
)

st.plotly_chart(fig)

#TEMP COMPARISION
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df["timestamp"],
        y=df["battery_temp_c"],
        name="Actual Temp"
    )
)
fig.add_trace(
    go.Scatter(
        x=ideal_df["timestamp"],
        y=ideal_df["battery_temp_c"],
        name="Ideal Temp"
    )
)
# fig.update_layout(
#     template = "plotly_dark",
#     height = 500,
#     showlegend = False,
#     title = "Actual Temp vs Ideal Temp"
# )
st.plotly_chart(fig, use_container_width=True)

#VOLTAGE COMPARISON
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df["timestamp"],
        y=df["battery_voltage_v"],
        name="Actual Voltage"
    )
)
fig.add_trace(
    go.Scatter(
        x=ideal_df["timestamp"],
        y=ideal_df["battery_voltage_v"],
        name="Ideal Voltage"
    )
)
st.plotly_chart(fig, use_container_width=True)

# EFFICIENCY SCORE CARD
actual_avg_soc = df["soc_percent"].mean()
ideal_avg_soc = ideal_df["soc_percent"].mean()
efficiency = (actual_avg_soc / ideal_avg_soc) * 100

st.metric("Battery Efficiency",f"{efficiency:.2f}%")

st.markdown("---")


#DISPLAY DATA
st.subheader("Processed Battery Data")
st.dataframe(df)
st.markdown("---")

#Caption at the end 
st.caption(
    "EV Battery Management System Analytics Platform"
)