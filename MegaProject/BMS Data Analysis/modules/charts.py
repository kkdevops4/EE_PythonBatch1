'''
pip install kaleido
'''

import plotly.express as px

def show_grid(fig):
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

def create_soc_chart(df):
    fig = px.line(
        df,
        x="timestamp",
        y="soc_percent",
        title="State of Charge Over Time",
        labels={
            "timestamp": "Time",
            "soc_percent": "SoC (%)"
            }
        )
    show_grid(fig)
    fig.write_image("output_data/soc_chart.png")

    return fig

def create_voltage_chart(df):
    fig = px.line(
        df,
        x="timestamp",
        y="battery_voltage_v",
        title="Battery Voltage Over Time",
        labels={
            "timestamp": "Time",
            "battery_voltage_v": "Voltage (V)"
            }
        )
    show_grid(fig)
    fig.write_image("output_data/voltage_chart.png")
    return fig

def create_current_chart(df):

    fig = px.line(
        df,
        x="timestamp",
        y="battery_current_a",
        title="Battery Current Over Time",
        labels={
            "timestamp": "Time",
            "battery_current_a": "Current (A)"
            }
        )
    show_grid(fig)
    fig.write_image("output_data/current_chart.png")
    return fig

def create_temp_chart(df):

    fig = px.line(
        df,
        x="timestamp",
        y="battery_temp_c",
        title="Battery Temperature Over Time",
        labels={
            "timestamp": "Time",
            "battery_temp_c": "Temperature (°C)"
            }
        )
    show_grid(fig)
    fig.add_hline(y=45,
                  line_dash="dash",
                  annotation_text="Warning Threshold (45°C)"
                  )

    fig.write_image("output_data/temp_chart.png")
    return fig
