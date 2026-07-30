from datetime import datetime


class HTMLReportGenerator:

    @staticmethod
    def create_html_report(
        df,
        pass_count,
        fail_count,
        not_executed_count,
        chart_path,
        output_html
    ):

        total_tc = len(df)

        generated_time = datetime.now().strftime(
            "%d-%b-%Y %I:%M %p"
        )

        pass_percentage = (
            pass_count / total_tc * 100
        ) if total_tc else 0

        fail_percentage = (
            fail_count / total_tc * 100
        ) if total_tc else 0

        not_executed_percentage = (
            not_executed_count / total_tc * 100
        ) if total_tc else 0

        # Generate table rows
        table_rows = ""

        for _, row in df.iterrows():

            status = str(row["Status"]).strip()

            if status == "Pass":
                status_badge = (
                    '<span class="pass-badge">PASS</span>'
                )

            elif status == "Fail":
                status_badge = (
                    '<span class="fail-badge">FAIL</span>'
                )

            else:
                status_badge = (
                    '<span class="not-badge">NOT EXECUTED</span>'
                )

            table_rows += f"""
            <tr>
                <td>{row['TC_ID']}</td>
                <td>{row['Test_Description']}</td>
                <td>{row['Ignition_ON/OFF']}</td>
                <td>{row['Vehicle_Speed_(km/h)']}</td>
                <td>{row['Expected_Result']}</td>
                <td>{row['Actual_Result']}</td>
                <td>{status_badge}</td>
                <td>{row['Remarks']}</td>
            </tr>
            """

        # Failed test cases
        failed_cards = ""

        failed_df = df[df["Status"] == "Fail"]

        for _, row in failed_df.iterrows():

            failed_cards += f"""
            <div class="failed-card">
                <h4>{row['TC_ID']}</h4>

                <p>
                    <b>Description:</b>
                    {row['Test_Description']}
                </p>

                <p>
                    <b>Remarks:</b>
                    {row['Remarks']}
                </p>
            </div>
            """

        html = f"""
<!DOCTYPE html>
<html>

<head>

<title>BCM Validation Report</title>

<style>

body {{
    font-family: Arial;
    background: #f4f6f9;
    margin: 30px;
}}

h1 {{
    color: #003366;
}}

.summary {{
    display: flex;
    gap: 20px;
}}

.card {{
    flex: 1;
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0px 2px 6px gray;
}}

.pass-card {{
    border-left: 6px solid green;
}}

.fail-card-summary {{
    border-left: 6px solid red;
}}

.not-card {{
    border-left: 6px solid orange;
}}

.pass-badge {{
    background: #d4edda;
    color: green;
    padding: 5px 10px;
    border-radius: 10px;
    font-weight: bold;
}}

.fail-badge {{
    background: #f8d7da;
    color: red;
    padding: 5px 10px;
    border-radius: 10px;
    font-weight: bold;
}}

.not-badge {{
    background: #fff3cd;
    color: orange;
    padding: 5px 10px;
    border-radius: 10px;
    font-weight: bold;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    background: white;
}}

th {{
    background: #003366;
    color: white;
    padding: 10px;
}}

td {{
    border: 1px solid #ddd;
    padding: 8px;
}}

tr:hover {{
    background: #f5f5f5;
}}

.failed-card {{
    background: #ffe5e5;
    border-left: 6px solid red;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 10px;
}}


.search-box {{
    width:350px;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
}}


.chart-container {{
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}}

.chart-container img {{
    border-radius: 10px;
    box-shadow: 0px 2px 8px gray;
}}
</style>
<script>

function searchTable() {{

    let input = document.getElementById(
        "searchInput"
    );

    let filter = input.value.toUpperCase();

    let table = document.getElementById(
        "reportTable"
    );

    let tr = table.getElementsByTagName(
        "tr"
    );

    for (let i = 1; i < tr.length; i++) {{

        let txtValue =
            tr[i].textContent ||
            tr[i].innerText;

        if (
            txtValue.toUpperCase()
            .indexOf(filter) > -1
        ) {{

            tr[i].style.display = "";

        }} else {{

            tr[i].style.display = "none";
        }}
    }}
}}

</script>
</head>

<body>

<h1>🚗 BCM Door Functionality Validation Report</h1>

<p>
<b>Generated On:</b>
{generated_time}
</p>

<div class="summary">

<div class="card pass-card">
<h2>{pass_count}</h2>
Passed
</div>

<div class="card fail-card-summary">
<h2>{fail_count}</h2>
Failed
</div>

<div class="card not-card">
<h2>{not_executed_count}</h2>
Not Executed
</div>

</div>

<br>

<h2>Execution Summary</h2>

<p>Total Test Cases : {total_tc}</p>
<p>Pass Percentage : {pass_percentage:.2f}%</p>
<p>Fail Percentage : {fail_percentage:.2f}%</p>
<p>Not Executed Percentage : {not_executed_percentage:.2f}%</p>
<h2>Execution Pie Chart</h2>


<div class="chart-container">

    <img src="{chart_path}" width="500">

</div>
<h2>Search Test Cases</h2>

<input
    type="text"
    id="searchInput"
    class="search-box"
    onkeyup="searchTable()"
    placeholder="Search by TC ID, Status, Description..."
>

<h2>Detailed Test Results</h2>

<table id="reportTable">

<tr>
<th>TC ID</th>
<th>Description</th>
<th>Ignition</th>
<th>Speed</th>
<th>Expected</th>
<th>Actual</th>
<th>Status</th>
<th>Remarks</th>
</tr>

{table_rows}

</table>
<br>

<h2>Failed Test Cases</h2>

{failed_cards}

</body>

</html>
"""

        with open(
            output_html,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        print(
            f"HTML Report Generated Successfully: "
            f"{output_html}"
        )
