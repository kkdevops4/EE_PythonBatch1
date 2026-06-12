import os
import pandas as pd
import matplotlib.pyplot as plt
import docx
from docx.shared import Inches
from docx2pdf import convert

# FUNCTIONS

def get_driver_state(score):
    if score >= 85:
        return "Alert"
    elif score >= 70:
        return "Moderate"
    elif score >= 50:
        return "Slight_Fatigue"
    else:
        return "Drowsy"


def get_driver_remark(attention):

    if attention >= 85:
        return ("Driver is highly alert and maintaining good attention throughout the journey. No signs of fatigue detected.")

    elif attention >= 70:
        return ("Driver shows moderate attention levels. Short breaks are recommended during long trips.")

    elif attention >= 50:
        return ("Driver is showing signs of fatigue. Continuous driving may affect safety and concentration.")

    else:
        return ("Driver is highly drowsy and at significant risk. Immediate rest is strongly recommended.")


def generate_driver_report(row, remark):

    return f"""
Driver ID           : {row['Driver_ID']}
Driver Name         : {row['Driver_names']}

Travel Time         : {row['Total_Time_Minutes']} Minutes
Distance Covered    : {row['Total_Distance_km']:.2f} km

Average Eye Closure : {row['Avg_Eye_Closure']:.2f} %
Average Blink Rate  : {row['Avg_Blink_Rate']:.2f} blinks/min
Average Head Pitch  : {row['Avg_Head_Pitch']:.2f}°

Attention Score     : {row['Avg_Attention_Score']:.2f}
Driver State        : {row['Final_State']}

Driver Assessment:
{remark}
"""

# READ CSV

csv_file = r"C:\Users\ia97974\Desktop\51856\EE_PythonBatch1\MegaProject\Driver_Monitoring_system\driver_monitoring_system_2.csv"

df = pd.read_csv(csv_file)

# ATTENTION SCORE

eye_score = 100 - df["Eye_Closure_Percentage"]

blink_score = 100 - (abs(15 - df["Blink_Rate"]) * 5)

head_score = 100 - (df["Head_Pitch_Angle"] * 4)

eye_score = eye_score.clip(0, 100)
blink_score = blink_score.clip(0, 100)
head_score = head_score.clip(0, 100)

df["Attention_Score"] = (eye_score * 0.60 + blink_score * 0.25 + head_score * 0.15).round(2)
 
states = []                            # eg.- states = ["Alert", "Moderate", "Slight Fatigue"]

for score in df["Attention_Score"]:
    states.append(get_driver_state(score))

df["State"] = states                  # Pandas creates a new column in data frame i.e State                      

# DRIVER SUMMARY

report = df.groupby(
    ["Driver_ID", "Driver_names"]
).agg({
    "Time_Minutes": "max",
    "Travel_Distance_km": "max",
    "Eye_Closure_Percentage": "mean",
    "Blink_Rate": "mean",
    "Head_Pitch_Angle": "mean",
    "Attention_Score": "mean"
}).reset_index()

final_state = df.groupby(["Driver_ID", "Driver_names"])["State"].last().reset_index()

report = report.merge(final_state,on=["Driver_ID", "Driver_names"])

report.columns = [
    "Driver_ID",
    "Driver_names",
    "Total_Time_Minutes",
    "Total_Distance_km",
    "Avg_Eye_Closure",
    "Avg_Blink_Rate",
    "Avg_Head_Pitch",
    "Avg_Attention_Score",
    "Final_State"
]

# CONSOLE REPORT

print("\n==============================")
print(" DRIVER WISE REPORT")
print("==============================\n")

for _, row in report.iterrows():

    attention = row["Avg_Attention_Score"]    # take the value in the column Avg_Attention_Score and store it in a variable called attention

    remark = get_driver_remark(attention)

    print(generate_driver_report(row,remark))

# INDIVIDUAL DRIVER GRAPHS

for _, row in report.iterrows():

    metrics = [
        row["Avg_Eye_Closure"],
        row["Avg_Blink_Rate"],
        row["Avg_Head_Pitch"],
        row["Avg_Attention_Score"]
    ]

    labels = [
        "Eye Closure %",
        "Blink Rate",
        "Head Pitch",
        "Attention Score"
    ]

    plt.figure(figsize=(10, 6))

    bars = plt.bar(labels,metrics,color=["red","orange","purple","green"])

    plt.title(f"Driver Performance Report\n{row['Driver_names']}(ID: {row['Driver_ID']})")

    plt.ylabel("Value")

    for bar in bars:

        plt.text(
            bar.get_x()
            + bar.get_width()/2,
            bar.get_height(),
            f"{bar.get_height():.1f}",
            ha="center",
            va="bottom"
        )

    plt.grid(axis="y", linestyle="--")

    plt.tight_layout()

    graph_file = (f"graphs/Driver_{row['Driver_ID']}_Performance.png")

    plt.savefig(graph_file,dpi=300,bbox_inches="tight")

    plt.close()

# COMPARISON GRAPH

driver_attention = report.set_index("Driver_names")["Avg_Attention_Score"]

plt.figure(figsize=(10, 6))

bars = plt.bar(
    driver_attention.index,
    driver_attention.values,
    color="skyblue"
)

for bar in bars:

    score = bar.get_height()

    if score >= 85:
        status = "Excellent"
    elif score >= 70:
        status = "Good"
    elif score >= 50:
        status = "Fatigued"
    else:
        status = "Drowsy"

    plt.text(
        bar.get_x()
        + bar.get_width()/2,
        score,
        f"{score:.1f}\n{status}",
        ha="center",
        va="bottom"
    )

plt.title("Average Attention Score by Driver")

plt.xlabel("Driver")
plt.ylabel("Attention Score")
plt.ylim(0, 100)

plt.grid(axis="y", linestyle="--")

plt.tight_layout()

comparison_graph = ("graphs/Driver_Attention_Comparison.png")

plt.savefig(comparison_graph,dpi=300,bbox_inches="tight")
plt.close()

# CREATE OUTPUT FOLDER

os.makedirs("graphs", exist_ok=True)       # exist_ok=True  If folder already exists don't give error. if we can't use this python crash second time.

# WORD REPORT

doc = docx.Document()

doc.add_heading("Driver Monitoring System Report",level=0)

for _, row in report.iterrows():

    attention = row["Avg_Attention_Score"]

    remark = get_driver_remark(attention)

    doc.add_heading(f"Driver: {row['Driver_names']} (ID: {row['Driver_ID']})",level=1)

    doc.add_paragraph(generate_driver_report(row,remark))

    graph_file = (f"graphs/Driver_{row['Driver_ID']}_Performance.png")

    if os.path.exists(graph_file):

        doc.add_picture(graph_file,width=Inches(5.5))
    doc.add_page_break()

# OVERALL COMPARISON GRAPH

doc.add_heading("Driver Attention Score Comparison",level=1)

if os.path.exists(comparison_graph):

    doc.add_picture(comparison_graph,width=Inches(6))

# SAVE WORD FILE

doc_file = ("Driver_Monitoring_Report.docx")
doc.save(doc_file)
print("\nWord Report Saved Successfully!")

# PDF CONVERSION

try:
    convert(doc_file)
    print("PDF Report Generated Successfully!")

except Exception as e:
    print("\nPDF Conversion Failed!")
    print(e)