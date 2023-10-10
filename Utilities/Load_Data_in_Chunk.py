import pandas as pd
total = 0
for chunk in pd.read_csv('aa.csv', chunksize=500):
    total += sum(chunk['peak'])
print(total)
