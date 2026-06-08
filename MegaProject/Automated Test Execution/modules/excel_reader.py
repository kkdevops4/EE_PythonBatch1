import pandas as pd


class ExcelReader:

    @staticmethod
    def read_excel(file_path):

        try:
            df = pd.read_excel(file_path)

            # Remove extra spaces from column names
            df.columns = df.columns.str.strip()

            print("\nExcel Loaded Successfully")
            print("Columns Found:")
            print(df.columns.tolist())

            return df

        except Exception as e:
            print(f"Error: {e}")
            return None