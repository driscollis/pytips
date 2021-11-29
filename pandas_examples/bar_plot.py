import numpy as np
import pandas as pd

df = pd.Series(np.random.randn(200),
               index=pd.date_range("1/1/2000",
                                   periods=200))

df.plot(kind="bar")