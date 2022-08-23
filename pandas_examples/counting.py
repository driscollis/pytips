import pandas as pd

# Read only the first 5 rows from a CSV file
df = pd.read_csv("books.csv", nrows=5)

author_counts = df["author"] == "Mike Driscoll"
print(author_counts.value_counts())

# Alternate way to count
author_counts = df["author"].value_counts()
print(f"Number of times 'Mike Driscoll' is an author = "
      f"{author_counts['Mike Driscoll']}")