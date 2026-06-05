import streamlit as st
import plotly.express as px
import pandas as pd


def show_speed_chart(df, speed_limit):
    print("Charts gets called")
    if df is None or df.empty:
        st.info("No data available for chart")
        return

    if "speed" not in df.columns:
        st.warning("Speed column missing")
        return

    df = df.copy()

    # -----------------------------
    # CLEAN SPEED (SAFE FIX)
    # -----------------------------
    df["speed"] = pd.to_numeric(df["speed"], errors="coerce")
    df = df.dropna(subset=["speed"])

    # -----------------------------
    # FIX TIMESTAMP SAFELY
    # -----------------------------
    if "timestamp" in df.columns:

        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.dropna(subset=["timestamp"])
        df = df.sort_values("timestamp")

        x_axis = "timestamp"

    else:
        # fallback safe index column
        df = df.reset_index()
        x_axis = "index"

    if df.empty:
        st.info("No valid data after cleaning")
        return

    # -----------------------------
    # COLOR LOGIC (FASTER + SAFE)
    # -----------------------------
    df["color"] = df["speed"].apply(
        lambda x: "red" if x > speed_limit else "lime"
    )

    # -----------------------------
    # PLOT (FIXED MODE)
    # -----------------------------
    fig = px.line(
        df,
        x=x_axis,
        y="speed",
        color="color",
        markers=True,
        title="Speed vs Time",
        color_discrete_map={
            "lime": "lime",
            "red": "red"
        }
    )

    # -----------------------------
    # SPEED LIMIT LINE
    # -----------------------------
    fig.add_hline(
        y=speed_limit,
        line_dash="dash",
        line_color="white",
        annotation_text=f"Speed Limit: {speed_limit}"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)