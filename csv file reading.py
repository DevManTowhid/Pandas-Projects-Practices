import pandas as pd

filecsv = pd.read_csv("large_dummy_data.csv", nrows=15)

print(filecsv)