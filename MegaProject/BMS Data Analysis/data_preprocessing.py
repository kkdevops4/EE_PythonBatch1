# =====================================================
# LIBRARY IMPORTS 
# =====================================================
import pandas as pd

# =====================================================
# READ EXCEL FILE
# =====================================================
# df = pd.read_excel("data/BMW_i3_24H_Clean_Reference.xlsx")
# df = pd.read_excel("data/BMW_i3_Abnormal_Thermal_Runaway.xlsx")
df = pd.read_excel("data/BMW_i3_Abnormal_Voltage_Collapse.xlsx")

print(df.head()) #show first 5 rows
print(df.info())
print(df.isnull().sum())

df["timestamp"] = pd.to_datetime(df["timestamp"])
print(df.info())

# =====================================================
# DATA SORTING
# =====================================================
df = (df.sort_values("timestamp").reset_index(drop=True))

# =====================================================
# CREATE HOUR COLUMN
# =====================================================
df["hour"] = df["timestamp"].dt.hour

# =====================================================
# SAVE AS EXCEL
# =====================================================
df.to_excel("processed_data/processed_battery_data.xlsx",index=False)
#if Index was true Pandas would save index as an extra column which we don't need

print("Processed file saved")
