from modules.excel_reader import ExcelReader
from modules.bcm_validator import BCMValidator
from modules.chart_generator import ChartGenerator
from modules.report_generator import ReportGenerator

# Uncomment when docx2pdf is installed
from modules.pdf_converter import PDFConverter

EXCEL_FILE = "data/bcm_testcases.xlsx"

# Read Excel
df = ExcelReader.read_excel(EXCEL_FILE)

if df is None:
    print("Excel loading failed.")
    exit()

# Store results
actual_results = []
remarks_list = []

# Execute BCM validation
for _, row in df.iterrows():

    actual_result, remarks = BCMValidator.validate(row)

    actual_results.append(actual_result)
    remarks_list.append(remarks)

# Add new columns
df["Actual_Result"] = actual_results
df["Remarks"] = remarks_list

# Compare Expected vs Actual
df["Status"] = df.apply(
    lambda row:
    "Pass"
    if str(row["Expected_Result"]).strip()
       ==
       str(row["Actual_Result"]).strip()
    else "Fail",
    axis=1
)

# Calculate statistics
total_tc = len(df)

pass_count = len(
    df[df["Status"] == "Pass"]
)

fail_count = len(
    df[df["Status"] == "Fail"]
)

print("\n========== EXECUTION SUMMARY ==========")
print(f"Total Test Cases : {total_tc}")
print(f"Passed           : {pass_count}")
print(f"Failed           : {fail_count}")
print("=======================================\n")

# Generate Pie Chart
ChartGenerator.generate(
    pass_count=pass_count,
    fail_count=fail_count,
    output_file="reports/pie_chart.png"
)

# Generate Word Report
ReportGenerator.create_report(
    df=df,
    pass_count=pass_count,
    fail_count=fail_count,
    chart_path="reports/pie_chart.png",
    output_docx="reports/BCM_Report.docx"
)

# Generate PDF (optional)

PDFConverter.convert_to_pdf(
    docx_file="reports/BCM_Report.docx",
    pdf_file="reports/BCM_Report.pdf"
)


# print("Report Generated Successfully")
# print("Word Report : reports/BCM_Report.docx")

# Uncomment after docx2pdf installation
# print("PDF Report  : reports/BCM_Report.pdf")