import streamlit as st


def sidebar_controls(df):
    st.sidebar.header("🎛️ Controls")

    # Safety check
    if df is None or df.empty:
        return df, 80

    df = df.copy()

    # -----------------------------
    # Vehicle filter
    # -----------------------------
    if "vehicle_id" in df.columns:
        vehicles = df["vehicle_id"].dropna().unique()

        if len(vehicles) > 0:
            selected_vehicle = st.sidebar.selectbox(
                "Select Vehicle",
                vehicles
            )

            df = df[df["vehicle_id"] == selected_vehicle]

    # -----------------------------
    # Speed limit slider
    # -----------------------------
    speed_limit = st.sidebar.slider(
        "Speed Limit",
        min_value=0,
        max_value=200,
        value=80,
        step=1
    )

    return df, speed_limit