# csv_to_sqlite.py

import sqlite3
import pandas as pd


def csv_to_sqlite(csv_file, sql_file):
    df = pd.read_csv(csv_file)
    with sqlite3.connect(sql_file) as conn:
        df.to_sql("Books", conn)

if __name__ == "__main__":
    csv_to_sqlite("books.csv", "books.db")