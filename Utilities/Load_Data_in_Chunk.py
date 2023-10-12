# Do the computations on the data of the specified chunk size
import pandas as pd
total = 0
for chunk in pd.read_csv('aa.csv', chunksize=500):
    total += sum(chunk['peak'])
print(total)

df_reader = pd.read_csv('aa.csv', chunksize=10) # df_reader is a generator
print(next(df_reader)) # Print the first chunk
print(next(df_reader))
