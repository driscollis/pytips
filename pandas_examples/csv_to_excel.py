# csv_to_excel.py

import pandas as pd


def csv_to_excel(csv_file, excel_file, sheet_name):
    df = pd.read_csv(csv_file)
    df.to_excel(excel_file, sheet_name=sheet_name)


if __name__ == "__main__":
    csv_to_excel("books.csv", "pandas_csv_to_excel.xlsx", "Books")