import plotly.express as px

def create_soc_chart(df):
    fig = px.line(
        df,
        x="timestamp",
        y="soc_percent",
        title="State of Charge Over Time"
    )

    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig