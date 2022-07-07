# excel_to_csv.py

import pandas as pd


def excel_to_csv(excel_file, csv_file, sheet_name=0):
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    df.to_csv(csv_file)


if __name__ == "__main__":
    excel_to_csv("books.xlsx", "pandas_books.csv")