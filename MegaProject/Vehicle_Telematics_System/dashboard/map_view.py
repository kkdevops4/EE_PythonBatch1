import streamlit as st
import pydeck as pdk
from dashboard.osrm_route import get_osrm_route


def show_map(df, df_filtered, speed_limit):

    st.subheader("🗺 Route Visualization")

    if df is None or df.empty:
        st.warning("No GPS data available")
        return

    df = df.dropna(subset=["latitude", "longitude"])

    if len(df) < 2:
        st.warning("Need at least 2 points for route")
        return

    # -----------------------------
    # START + END (last trip)
    # -----------------------------
    start_lat = df.iloc[0]["latitude"]
    start_lon = df.iloc[0]["longitude"]

    end_lat = df.iloc[-1]["latitude"]
    end_lon = df.iloc[-1]["longitude"]

    # -----------------------------
    # OSRM ROUTE
    # -----------------------------
    path = get_osrm_route(start_lat, start_lon, end_lat, end_lon)

    if not path:
        st.error("Route not found")
        return

    # -----------------------------
    # ROUTE LINE (MAIN FEATURE)
    # -----------------------------
    route_layer = pdk.Layer(
        "PathLayer",
        data=[{"path": path}],
        get_path="path",
        get_color=[0, 255, 180],   # green-blue like your image
        width_scale=6,
        width_min_pixels=4
    )

    # -----------------------------
    # START MARKER
    # -----------------------------
    start_layer = pdk.Layer(
        "ScatterplotLayer",
        data=[{"lat": start_lat, "lon": start_lon}],
        get_position=["lon", "lat"],
        get_fill_color=[0, 200, 0],
        get_radius=120
    )

    # -----------------------------
    # END MARKER
    # -----------------------------
    end_layer = pdk.Layer(
        "ScatterplotLayer",
        data=[{"lat": end_lat, "lon": end_lon}],
        get_position=["lon", "lat"],
        get_fill_color=[255, 0, 0],
        get_radius=120
    )

    # -----------------------------
    # MAP VIEW (CLEAN STYLE)
    # -----------------------------
    view_state = pdk.ViewState(
        latitude=(start_lat + end_lat) / 2,
        longitude=(start_lon + end_lon) / 2,
        zoom=11,
        pitch=0
    )

    deck = pdk.Deck(
        map_style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
        layers=[route_layer, start_layer, end_layer],
        initial_view_state=view_state
    )

    st.pydeck_chart(deck)