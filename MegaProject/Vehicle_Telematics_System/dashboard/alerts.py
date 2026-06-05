import streamlit as st


def show_alerts(df, speed_limit):

    st.subheader("🚨 Alerts")

    if "speed" not in df.columns:
        return

    overspeed = df[df["speed"] > speed_limit]

    if len(overspeed) > 0:

        st.error(
            f"Overspeed Events: {len(overspeed)}"
        )

        st.dataframe(
            overspeed,
            use_container_width=True
        )

    else:

        st.success(
            "✅ All vehicles within speed limit"
        )