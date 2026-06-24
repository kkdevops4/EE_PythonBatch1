import streamlit as st
import plotly.express as px
from modules.analytics import *

def show_grid(fig):
    fig.update_xaxes(showgrid = True)
    fig.update_yaxes(showgrid = True)


def dashboard():
    st.set_page_config(
    page_title="EV Battery Analysis",
    page_icon="⚡",
    layout="wide"
)
    df = load_data("processed_data/processed_battery_data.xlsx")

# =====================================================
# TITLE
# =====================================================
    st.title("BATTERY MANAGEMENT SYSTEM")
    st.caption("EV Battery Analytics Dashboard")

# =====================================================
# ASSIGNING VALUES
# =====================================================
    soc = soc_summary(df)
    soh = soh_summary(df)
    temp = temperature_summary(df)
    voltage = voltage_summary(df)
    current = current_summary(df)
    dataset = dataset_summary(df)

    latest_soc = soc["Latest SoC"]
    latest_soh = soh["Latest SoH"]
    latest_voltage = voltage["Latest Voltage"]
    peak_temp = temp["Maximum Temperature"]
    avg_temp = temp["Average Temperature"]

    temp_status = temperature_status(peak_temp)
    health_status = battery_health_status(latest_soh)
    overall_status = overall_condition(latest_soh, peak_temp)
    soc_condition = soc_status(latest_soc)

    charging = charging_summary(df)

    charging_hours = charging["Charging Hours"]
    charging_status = charging["Charging Status"]

# =====================================================
# DATASET INFORMATION
# =====================================================
    st.subheader("Dataset Information")
    
    col1, col2, col3 = st.columns(3)

    col1.metric("Records", dataset["Record Count"])
    col2.metric("Start Time", str(dataset["Start Time"]))
    col3.metric("End Time", str(dataset["End Time"]))

    st.divider()

# =====================================================
# BATTERY OVERVIEW
# =====================================================
    st.subheader("Battery Overview")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric("Latest SoC", f"{latest_soc}%")
    col2.metric("Latest SoH", f"{latest_soh}%")
    col3.metric("Latest Voltage", f"{latest_voltage} V")
    col4.metric("Peak Temperature", f"{peak_temp} °C")
    col5.metric("Charging Time", f"{charging_hours} hrs")
    col6.metric("Average Temperature", f"{avg_temp} °C")

    st.divider()

# ==========================================
# SIDEBAR - QUICK STATS
# ==========================================

    st.sidebar.header("BATTERY OVERVIEW STATS")

    st.sidebar.metric("Latest SoC",f"{latest_soc}%")
    st.sidebar.metric("Latest SoH",f"{latest_soh}%")
    st.sidebar.metric("Latest Voltage",f"{latest_voltage} V")
    st.sidebar.metric("Peak Temperature",f"{peak_temp} °C")
    st.sidebar.metric("Charging Time",f"{charging_hours} hrs")
    st.sidebar.metric("Average Temperature",f"{avg_temp} °C")

# =====================================================
# BATTERY STATUS
# =====================================================
    st.subheader("Battery Status Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("SoC Status", soc_condition)
    col2.metric("Temperature Status", temp_status)
    col3.metric("Battery Health", health_status)

    st.divider()

# =====================================================
# STATE OF CHARGE TRENDS
# =====================================================
    st.subheader("State of Charge Trend")

    fig = px.line(
        df,
        x = "timestamp",
        y = "soc_percent",
        title = "State of Charge Over Time"
)
    show_grid(fig)

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
    show_grid(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(f"""
    ### Voltage Summary

    - Minimum Voltage: {voltage["Minimum Voltage"]} V
    - Maximum Voltage: {voltage["Maximum Voltage"]} V
    - Average Voltage: {voltage["Average Voltage"]} V
    """)

    st.caption(
        "Voltage may rise during charging and drop under heavy load."
)

    fig = px.line(
        df,
        x = "timestamp",
        y = "battery_current_a", 
        title = "Battery current over time" 
)
    show_grid(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
)

    st.info("""
    Positive Current = Battery Discharging while Driving

    Negative Current = Battery Charging

    Current Near Zero = Idle State
    """)

    st.markdown(f"""
    ### Current Summary

    - Maximum Discharge Current: {current["Maximum Discharge Current"]} A
    - Maximum Charge Current: {current["Maximum Charge Current"]} A
    - Average Current: {current["Average Current"]} A
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
    show_grid(fig)

    fig.add_hline(
        y = 45,
        line_dash = "dash",
        annotation_text = "Warning Threshold (45°C)"
)

    st.plotly_chart(
        fig,
        use_container_width=True
)

    min_temp = temp["Minimum Temperature"]

    st.info(f"Maximum Temperature: {peak_temp} °C")
    st.info(f"Minimum Temperature: {min_temp} °C")

    if temp_status == "Warning":
        st.error("Temperature exceeded the warning threshold")
    else:
        st.success("Temperature within safe limits.")

    st.caption("Higher temperatures may indicate heavy vehicle usage, fast charging, or cooling system inefficiencies.")

    st.divider()

# =====================================================
# SOC VS SPEED
# =====================================================
    st.subheader("SoC vs Vehicle Speed")

    fig = px.scatter(
        df,
        x = "vehicle_speed_kmph",
        y = "soc_percent",
        title = "SoC vs Vehicle Speed"
)
    show_grid(fig)

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    This chart shows how battery State of Charge varies with vehicle speed.
    Clusters at higher speeds may indicate faster battery depletion.
    """)

    st.divider()

# =====================================================
# SYSTEM STATUS
# =====================================================
    st.subheader("System Status")

    if overall_status == "Normal Operation":
        st.success("Battery operating within expected limits.")
    elif overall_status == "Monitor Battery Condition":
        st.warning("Battery health should be monitored.")
    else:
        st.error("Battery requires attention.")

    st.divider()

# =====================================================
# BATTERY SUMMARY 
# =====================================================
    min_soc = soc["Minimum SoC"]
    max_soc = soc["Maximum SoC"]
# =====================================================

    st.markdown(f"""
    ### Battery Health Summary

    - Battery health remained at **{latest_soh}% SoH**.

    - Health Status: **{health_status}**

    - State of charge ranged between **{min_soc}%** and **{max_soc}%**.

    - State of charge Status: **{soc_condition}**

    - Charging Activity: **{charging_status}**

    - Total charging duration was approximately **{charging_hours} hours**.

    - Maximum battery temperature reached **{peak_temp}°C**.

    - Temperature Status: **{temp_status}**

    - Overall Battery Condition: **{overall_status}**
    """)

    st.divider()
    
    st.caption(
    "EV Battery Management System Analytics Platform | BMW i3 Dataset | Version 2.0"
)

# =====================================================
# TESTING
# =====================================================
if __name__ == "__main__":
    dashboard()