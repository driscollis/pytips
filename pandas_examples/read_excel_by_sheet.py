# read_excel_by_sheet.py

import pandas as pd

sheet_one_data = pd.read_excel('sample.xlsx', sheet_name=0)
sheet_two_data = pd.read_excel('sample.xlsx', sheet_name="Sales")

print(sheet_one_data)
print(sheet_two_data)