import streamlit as st

st.set_page_config(
    page_title="Telematics Dashboard",
    page_icon="🚗",
    layout="wide"
)

from dashboard.dashboard import run_dashboard


def main():
    run_dashboard()


if __name__ == "__main__":
    main()