import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

def battery_health_summary(df):
    summary = {
        "Current SOH": round(df["soh_percent"].iloc[-1], 2),
        "Average SOH": round(df["soh_percent"].mean(), 2),
        "Minimum SOH": round(df["soh_percent"].min(), 2),
        "Maximum SOH": round(df["soh_percent"].max(), 2)
    }
    return summary

def soc_analysis(df):
    summary = {
        "Current SOC": round(df["soc_percent"].iloc[-1], 2),
        "Average SOC": round(df["soc_percent"].mean(), 2),
        "Minimum SOC": round(df["soc_percent"].min(), 2),
        "Maximum SOC": round(df["soc_percent"].max(), 2)
    }
    return summary

def hourly_soc_trend(df):
    hourly = (
        df
        .groupby("hour")["soc_percent"]
        .mean()
        .reset_index()
    )
    return hourly

def temperature_analysis(df):
    summary = {
        "Average Temp": round(df["battery_temp_c"].mean(), 2),
        "Maximum Temp": round(df["battery_temp_c"].max(), 2),
        "Minimum Temp": round(df["battery_temp_c"].min(), 2)
    }
    return summary

def hourly_temperature_trend(df):
    hourly = (
        df
        .groupby("hour")["battery_temp_c"]
        .mean()
        .reset_index()
    )
    return hourly

def charging_analysis(df):
    return (
        df["battery_status"]
        .value_counts()
        .reset_index()
    )

def severity_analysis(df):
    return (
        df["severity"]
        .value_counts()
        .reset_index()
    )

def power_analysis(df):
    summary = {
        "Average Power":
            round(df["power_kw"].mean(), 2),
        "Maximum Power":
            round(df["power_kw"].max(), 2),
        "Minimum Power":
            round(df["power_kw"].min(), 2)
    }
    return summary

def generate_analytics(df):
    results = {
        "battery_health":
            battery_health_summary(df),
        "soc":
            soc_analysis(df),
        "temperature":
            temperature_analysis(df),
        "power":
            power_analysis(df)
    }
    return results

 