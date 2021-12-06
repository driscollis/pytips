import pandas as pd

df = pd.DataFrame([[100, 433, 10], [34, 10, 0], [75, 125, 5]],
                  index=['Python 101', 'Python 201', 'wxPython'],
                  columns=['Amazon', 'Leanpub', 'Gumroad'])
df.to_excel('pandas_to_excel.xlsx', sheet_name='Books')