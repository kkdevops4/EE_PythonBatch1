import streamlit as st
import pandas as pd

from config.firebase_config import db

from dashboard.sidebar import sidebar_controls
from dashboard.alerts import show_alerts
from dashboard.map_view import show_map
from dashboard.charts import show_speed_chart


@st.cache_data(ttl=30)
def load_data(limit_count=30):

    docs = db.collection("telemetry").limit(limit_count).stream()

    data = []

    for doc in docs:
        data.append(doc.to_dict())

    return pd.DataFrame(data)


def clean_data(df):

    for col in ["latitude", "longitude", "speed"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["latitude", "longitude"])

    if "timestamp" in df.columns:
        try:
            # df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce")
            df["timestamp"] = pd.to_datetime(pd.to_numeric(df["timestamp"], errors="coerce"), unit="s", errors="coerce")
            df = df.dropna(subset=["timestamp"])
            df = df.sort_values("timestamp")
        except:
            pass

    return df


def show_kpis(df):

    st.subheader("📊 Fleet Statistics")

    col1, col2, col3 = st.columns(3)

    if "speed" in df.columns:

        col1.metric(
            "🚀 Max Speed",
            f"{df['speed'].max():.1f} km/h"
        )

        col2.metric(
            "⚡ Avg Speed",
            f"{df['speed'].mean():.1f} km/h"
        )

        col3.metric(
            "🐢 Min Speed",
            f"{df['speed'].min():.1f} km/h"
        )


def run_dashboard():

    st.title("🚗 Smart Fleet Dashboard")
    st.caption("Live Vehicle Tracking + Route History")

    try:
        df = load_data()

    except Exception as e:
        st.error(f"Firestore Error: {e}")
        return

    if df.empty:
        st.warning("No telemetry data found")
        return

    df = clean_data(df)

    df_filered, speed_limit = sidebar_controls(df)

    show_kpis(df_filered)

    show_alerts(df_filered, speed_limit)

    st.divider()

    show_map(df, df_filered, speed_limit)

    show_speed_chart(df_filered, speed_limit)

    with st.expander("📦 View Data"):
        st.dataframe(df_filered, use_container_width=True)