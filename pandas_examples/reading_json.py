import numpy as np
import pandas as pd

df = pd.read_json("https://api.github.com/users/driscollis/repos?perpage=100")
columns = ["name", "stargazers_count", "forks"]

# Get the top 10 repos sorted by stargazer count
df[columns].sort_values("stargazers_count", ascending=False).head(10)