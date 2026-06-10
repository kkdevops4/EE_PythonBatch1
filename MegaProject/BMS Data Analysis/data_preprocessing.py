import pandas as pd

# df = pd.read_csv(
#     "data/BMWi3_22kWh_24h_battery_timeline.csv",
#     sep="\t"
# )

df = pd.read_excel("data/BMWi3_22kWh_24h_battery_timeline.xlsx")

print(df.head())

#Check dataset for null values
print(df.info())
print(df.isnull().sum())

#Convert to timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

#Sort by time - Understand
df = df.sort_values("timestamp")
df = df.reset_index(drop=True) 

#Data cleaning part 1
df["soc_percent"] = df["soc_percent"].clip(0,100)

df["soh_percent"] = df["soh_percent"].clip(0,100)

df["battery_temp_c"] = df["battery_temp_c"].clip(-20,70)

df["battery_voltage_v"] = df["battery_voltage_v"].clip(250,450)

#Hour Col Creation 
df["hour"] = df["timestamp"].dt.hour


#Charging or Discharging Status - Understand
def battery_status(current):

    if current > 1:
        return"Discharging"
    elif current < -1:
        return"Charging"
    else:
        return"Idle"

df["battery_status"] = df["battery_current_a"].apply(battery_status)    

#Temperature Difference
df["temp_difference"] = (
    df["battery_temp_c"] -
    df["battery_temp_c"].mean()
)

#Anomaly detection
df["severity"] = "Normal"

df.loc[
    df["battery_temp_c"] > 40,
    "severity"
] = "Warning"

df.loc[
    df["battery_temp_c"] > 50,
    "severity"
] = "Critical"

df.loc[
    df["soc_percent"] < 15,
    "severity"
] = "Warning"

df.loc[
    df["soc_percent"] < 5,
    "severity"
] = "Critical"

print(df["severity"].value_counts())


#Summary STATS 
summary = {
    "Current SOC": round(df["soc_percent"].iloc[-1],2),
    "Current SOH": round(df["soh_percent"].iloc[-1],2),
    "Average Temperature": round(df["battery_temp_c"].mean(),2),
    "Maximum Temperature": round(df["battery_temp_c"].max(),2),
    "Minimum SOC": round(df["soc_percent"].min(),2),
    "Total Records": len(df)
}

print(summary)


#Save as csv
df.to_csv(
    "processed_data/processed_battery_data.csv",
    index=False
)

print("Processed file saved")