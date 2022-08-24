import pandas as pd

a = [1, 7, 2]

series = pd.Series(a)
print(series)

indexed_series = pd.Series(a, index = ["x", "y", "z"])
print(indexed_series)
