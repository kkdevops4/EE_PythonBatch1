"""
analytics.py

Contains all battery analytics calculations used by:
- dashboard.py
- report.py
- main.py

Functions include:
- SoC analysis
- SoH analysis
- Temperature analysis
- Charging analysis
- Voltage analysis
- Current analysis
- Battery health evaluation
"""

# =====================================================
# LOAD DATA
# =====================================================
from modules.data_preprocessing import load_data

# =====================================================
# CALCULATE DATASET SUMMARY
# =====================================================
def dataset_summary(df):
    return {
        "Record Count": len(df),
        "Start Time": df["timestamp"].min(),
        "End Time": df["timestamp"].max()
    }

# =====================================================
# CALCULATE SOC INSIGHTS
# =====================================================
def soc_summary(df):
    summary = {
        "Latest SoC": round(df["soc_percent"].iloc[-1], 2),
        "Average SoC": round(df["soc_percent"].mean(), 2),
        "Minimum SoC": round(df["soc_percent"].min(), 2),
        "Maximum SoC": round(df["soc_percent"].max(), 2)
    }
    return summary

def soc_status(latest_soc):
    if latest_soc > 80:
        return "High Charge"
    elif latest_soc > 30:
        return "Normal"
    else:
        return "Low Battery"

# =====================================================
# CALCULATE SOH INSIGHTS
# =====================================================
def soh_summary(df):
    summary = {
        "Latest SoH": round(df["soh_percent"].iloc[-1], 2),
        "Average SoH": round(df["soh_percent"].mean(), 2),
        "Minimum SoH": round(df["soh_percent"].min(), 2),
        "Maximum SoH": round(df["soh_percent"].max(), 2)
    }
    return summary

# =====================================================
# CALCULATE TEMPERATURE INSIGHTS
# =====================================================
def temperature_summary(df):
    summary = {
        "Average Temperature": round(df["battery_temp_c"].mean(), 2),
        "Minimum Temperature": round(df["battery_temp_c"].min(), 2),
        "Maximum Temperature": round(df["battery_temp_c"].max(), 2)
    }
    return summary

def temperature_status(max_temp):
    if max_temp > 45:
        return "Warning"
    else:
        return "Safe"

# =====================================================
# CALCULATE POWER INSIGHTS
# =====================================================
def power_summary(df):
    summary = {
        "Average Power": round(df["power_kw"].mean(), 2),
        "Maximum Power": round( df["power_kw"].max(), 2),
        "Minimum Power": round(df["power_kw"].min(),2)
    }
    return summary

# =====================================================
# CALCULATE CHARGING INSIGHTS
# =====================================================
def charging_summary(df):
    charging_rows = (df["state"] == "Charging").sum()
    #DATASET SAMPLED EVERY 10 SECONDS
    charging_hours = round((charging_rows * 10) / 3600,2 )

    if charging_hours == 0:
        charging_status = "No charging activity detected"
    elif charging_hours < 2:
        charging_status = "Light charging activity"
    elif charging_hours < 5:
        charging_status = "Moderate charging activity"
    else:
        charging_status = "High charging activity"

    return {"Charging Hours": charging_hours,"Charging Status": charging_status}

# =====================================================
# CALCULATE VOLTAGE INSIGHTS  
# =====================================================
def voltage_summary(df):
    return {
        "Latest Voltage":round(df["battery_voltage_v"].iloc[-1], 2),
        "Minimum Voltage":round(df["battery_voltage_v"].min(), 2),
        "Maximum Voltage":round(df["battery_voltage_v"].max(), 2),
        "Average Voltage":round(df["battery_voltage_v"].mean(), 2)
    }

# =====================================================
# CALCULATE CURRENT INSIGHTS   
# =====================================================
def current_summary(df):
    return {
        "Maximum Discharge Current":round(df["battery_current_a"].max(), 2),
        "Maximum Charge Current":round(df["battery_current_a"].min(), 2),
        "Average Current":round(df["battery_current_a"].mean(),2)
    }


# =====================================================
# CALCULATE BATTERY HEALTH STATUS   
# =====================================================
def battery_health_status(latest_soh):
    if latest_soh >= 95:
        return "Excellent"
    elif latest_soh >= 90:
        return "Good"
    elif latest_soh >= 80:
        return "Moderate Degradation"
    else:
        return "Attention Required"
    
# =====================================================
# OVERALL BATTERY CONDITION
# =====================================================
def overall_condition(latest_soh, max_temp):
    if latest_soh < 80 or max_temp > 45:
        return "Attention Required"
    elif latest_soh < 90:
        return "Monitor Battery Condition"
    else:
        return "Normal Operation"
    

# =====================================================
# TESTING
# =====================================================
if __name__ == "__main__": 
    df = load_data("processed_data/processed_battery_data.xlsx")

    print(dataset_summary(df))
    print(soc_summary(df))
    print(soh_summary(df))
    print(temperature_summary(df))
    print(power_summary(df))
    print(charging_summary(df))
    print(voltage_summary(df))
    print(current_summary(df))

    latest_soc = soc_summary(df)["Latest SoC"]
    latest_soh = soh_summary(df)["Latest SoH"]
    max_temp = temperature_summary(df)["Maximum Temperature"]

    print(soc_status(latest_soc))
    print(temperature_status(max_temp))
    print(battery_health_status(latest_soh))
    print(overall_condition(latest_soh, max_temp))

    print("Analytics completed successfully")