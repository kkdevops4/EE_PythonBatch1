from analytics import *
from charts import *

df = load_data("processed_data/processed_battery_data.xlsx")

fig = create_soc_chart(df)

fig.write_image("output_data/soc_chart.png")