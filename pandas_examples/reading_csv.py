import pandas as pd

# Read only the first 5 rows from a CSV file
df = pd.read_csv("books.csv", nrows=5)
print(df)

df = pd.read_csv("books.csv", nrows=5, usecols=["author", "book_title"])
print(df)

# Extract just the author column
authors = df['author']
print(type(authors))