# Compute built-in summary statistics
df["column_name_1"].mean()
df[df["column_name_1"] == "group1"]["column_name_2"].mean() # calculate the mean by the specific group
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

# Drop the records with the duplicate values on variables
df.drop_duplicates(subset=["column_name_1", "column_name_2"])

# Count the categorical variable
df["column_name_1"].value_counts() # Count the number of each categorical level
df["column_name_1"].value_counts(sort=True) # Sort the count
df["column_name_1"].value_counts(normalize=True) # Count the proportion of each categorical level

# Calculate one or multiple grouped summary statistics
df.groupby("group_column")["column_name_1"].mean()
df.groupby("group_column")["column_name_1"].agg([mean, max, sum])
df.groupby(["group_column_1", "group_column_2"])["column_name_1"].mean()
df.groupby(["group_column_1", "group_column_2"])[["column_name_1", "column_name_2"]].mean()


