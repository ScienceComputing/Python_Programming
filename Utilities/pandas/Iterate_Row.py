import pandas as pd
import numpy as np

num_rows = 10000
num_columns = 20
data = np.random.rand(num_rows, num_columns)
column_names = [f"Column_{i+1}" for i in range(num_columns)]
df = pd.DataFrame(data, columns=column_names)
print(df.head())

df_generator = df.iterrows()
first_row = next(df_generator)
second_row = next(df_generator)
print(first_row, second_row)
