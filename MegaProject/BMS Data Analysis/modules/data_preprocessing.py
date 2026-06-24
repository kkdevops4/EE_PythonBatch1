# =====================================================
# LIBRARY IMPORTS 
# =====================================================
import pandas as pd

# =====================================================
# LOAD DATA FUNCTION
# =====================================================
def load_data(file_path):
    return pd.read_excel(file_path)

# =====================================================
# PREPROCESSING FUNCTION
# =====================================================
def preprocessing():
    print("Loading Dataset")
    # df = pd.read_excel(file_path)
    # df = pd.read_excel("data/BMW_i3_24H_Clean_Reference.xlsx")
    # df = pd.read_excel("data/BMW_i3_Abnormal_Thermal_Runaway.xlsx")
    # df = pd.read_excel("data/BMW_i3_Abnormal_Voltage_Collapse.xlsx")
    # df = pd.read_excel("data/BMW_i3_Golden_Reference_v2.xlsx")
    df = pd.read_excel("data/BMW_i3_Realistic_Pune_Summer_v2.xlsx")
    # df = pd.read_excel("data/BMW_i3_Abnormal_Fault_v2.xlsx")

    print("Checking missing values.")
    missing_values = df.isnull().sum().sum()

    if missing_values == 0:
        print("No missing values found.")
    else:
        print(f"{missing_values} missing values detected.")

    print("Converting timestamps")
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    print("Sorting records")
    df = (df.sort_values("timestamp").reset_index(drop=True))

    print("Creating Hour Column")
    df["hour"] = df["timestamp"].dt.hour

    print("Saving Processed dataset")
    df.to_excel("processed_data/processed_battery_data.xlsx",index=False)

    print("Processed file saved")

    return df


# =====================================================
# TESTING
# =====================================================
if __name__ == "__main__":
    preprocessing()