# Compute built-in summary statistics
df["column_name_1"].mean()
df["column_name_1"].median()
df["column_name_1"].mode()
df["column_name_1"].min()
df["column_name_1"].max()
df["column_name_1"].var()
df["column_name_1"].std()
df["column_name_1"].sum()
df["column_name_1"].quantile()

# Example: find the oldest and youngest birth date
df["birthdate"].min()
df["birthdate"].max()

# Compute custom summary statistics
def pct90(column):
    return column.quantile(90)

def pct70(column):
    return column.quantile(70)

df["column_name_1"].agg(pct90)
df[["column_name_1”, "column_name_2"]].agg(pct90)
df["column_name_1"].agg([pct90, pct70])

# Build a custom IQR function and mix it with np.median
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
df["column_name_1"].agg(iqr)

import numpy as np
print(df[["column_name_1", "column_name_2", "column_name_3"]].agg([iqr, np.median]))

# Compute cumulative statistics - return an entire column, not a single number
df["column_name_1"].cumsum()
df["column_name_1"].cummax()
df["column_name_1"].cummin()
df["column_name_1"].cumprod()


