# Topic: slice and index DataFrames
# Show the explicit column and row indices
df.columns
df.index

# Set a column as the row index
df.set_index("column_name_1") # Index values in this column can be repetitive 
# Reset the row index as default
df.reset_index()
# Reset the row index as default and drop the previous index such that the previous index will not appear as a column
df.reset_index(drop=True)

# Subset the rows
df[df["column_name_1"].isin(["value_1", "value_2"])] # This is a cumbersome way
df.set_index("column_name") # We first set the variable to be filtered as the index
df.loc[["value_1", "value_2"]] # We then use loc to filter on index values
df.loc["value_1"]

# Set multiple columns as the row index => create multi-level/hierarchical indices 
df.set_index(["column_name_1", "column_name_2"]) # The index level of column_name_2 is nested inside of the index level of column_name_1
# Subset the outer index level with a list
df.loc[["value_1", "value_2"]]
# Subset the inner index level with a list of tuples
df.loc[[("val_1_for_col_1", "val_1_for_col_2"), ("val_2_for_col_1", "val_2_for_col_2")]]

# Make the sorting by index values
df.sort_index() # By default, this function sorts all index levels from outer to inner in ascending order
# Control the sorting level and order
df.sort_index(level=["col_name_1", "col_name_2"], ascending=[True, False])
