import os
import subprocess
import sys


from modules.data_preprocessing import preprocessing
from modules.report import create_report

def main():

    print("Running preprocessing...")
    preprocessing()

    print("Generating report...")
    create_report()

    print("Launching dashboard...")
    subprocess.run([
    sys.executable,
    "-m",
    "streamlit",
    "run",
    "modules/dashboard.py"
])

if __name__ == "__main__":
    main()