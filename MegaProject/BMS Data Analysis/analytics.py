# =====================================================
# LIBRARY IMPORTS 
# =====================================================
import pandas as pd

# =====================================================
# LOAD DATA
# =====================================================
def load_data(file_path):
    df = pd.read_excel(file_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

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

# =====================================================
# CALCULATE POWER INSIGHTS
# =====================================================
def power_summary(df):
    summary = {
        "Average Power": round(df["power_kw"].mean(), 2),
        "Maximum Power": round( df["power_kw"].max(), 2)
    }
    return summary

# =====================================================
# TESTING
# =====================================================
if __name__ == "__main__": #Only run this code if this file is the program's starting point.
    df = load_data("processed_data/processed_battery_data.xlsx")

    print(soc_summary(df))
    print(soh_summary(df))
    print(temperature_summary(df))
    print(power_summary(df))
    print("Analytics done")