# EV Battery Management System (BMS) Data Analytics Platform

This project is a Python-based EV Battery Management System (BMS) analytics platform developed to monitor, analyze, visualize, and report battery performance data. Using BMW i3 battery telemetry data, the system performs battery health analysis, charging behavior monitoring, temperature tracking, dashboard visualization, and automated report generation.

### Current Features

* State of Charge (SoC) analysis
* State of Health (SoH) monitoring
* Voltage and current trend analysis
* Temperature trend analysis and alert monitoring
* Charging and discharging behavior analysis
* SoC vs Vehicle Speed analytics
* Battery condition assessment
* Interactive Streamlit dashboard
* Automated Word and PDF report generation
* Plotly-based data visualizations

### Project Architecture

#### 1. Data Processing Module

* Data loading and validation
* Timestamp processing
* Data cleaning and preparation

#### 2. Analytics Module

* Battery health analytics
* SoC and SoH analysis
* Temperature monitoring
* Charging behavior analysis
* Performance summary generation

#### 3. Dashboard Module

* Streamlit-based interactive dashboard
* KPI monitoring
* Plotly visualizations
* Alert and status monitoring

#### 4. Reporting Module

* Automated report generation
* Word (.docx) export
* PDF export
* KPI summaries and charts

### Technologies Used

* Python
* Pandas
* Streamlit
* Plotly
* python-docx
* docx2pdf
* Kaleido

### Installation

Clone the repository and install all dependencies:

```bash
py -m pip install -r requirements.txt

### Current Status

###Run the dashboard

```bash
py -m streamlit run dashboard.py

###Create Report

```bash
python report.py

Version 2.0 is functional and capable of:

* Processing EV battery telemetry data
* Performing battery analytics
* Generating interactive dashboards
* Creating professional Word and PDF reports

### Future Enhancements

* Energy consumption analysis (kWh)
* Charge cycle estimation
* Advanced battery degradation analytics
* Machine Learning based anomaly detection
* Real-time monitoring capabilities
* Cloud integration and data storage

### Long-Term Goal

To develop a scalable EV Battery Analytics Platform capable of real-time monitoring, automated reporting, intelligent battery diagnostics, and predictive maintenance analytics.
