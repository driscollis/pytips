import pandas as pd

df = pd.DataFrame(dict(departure=["DSM", "DSM", "LAX", "LAX", "DFW", "DSM"],
                      arrival=["ORD", "DFW", "DFW", "ORD", "ATL", "ATL"],
                      airlines=["Delta", "AA", "United", "SouthWest", "AA", "United"]))
pd.crosstab(index=[df["departure"], df["airlines"]],
            columns=[df["arrival"]],
            rownames=["departure", "airlines"],
            colnames=["arrival"],
            margins=True
           )
