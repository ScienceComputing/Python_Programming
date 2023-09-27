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

# Slicing and subsetting using loc method
# Subset the rows
df[df["column_name_1"].isin(["value_1", "value_2"])] # This is a cumbersome way to select eligible rows
df.set_index("column_name") # Set the variable to be filtered as the index
df.loc[["value_1", "value_2"]] # We then use loc to filter on index values; here we select that rows that meet 2 values; Notice that .loc[] makes our code less burdensome to maintain and easy for our collaborators to read 
df.loc["value_1"]

# Set multi-level/hierarchical indices made out of multiple columns when one category is nested inside another category
df.set_index(["column_name_1", "column_name_2"]) # The index level of column_name_2 is nested inside of the index level of column_name_1
# Subset the outer index level with a list
df.loc[["value_1", "value_2"]]
# Subset the inner index level with a list of tuples
df.loc[[("val_1_for_col_1", "val_1_for_col_2"), ("val_2_for_col_1", "val_2_for_col_2")]]

# Make the sorting by index values
df.sort_index() # By default, this function sorts all index levels from outer to inner in ascending order.
# Control the sorting level and order
df.sort_index(level=["col_name_1", "col_name_2"], ascending=[True,False])
df.sort_index(level="col_name_1")

# Sort the row index before slicing
df.set_index(["col_name_1", "col_name_2"]) .sort_index()
df.loc["val_1":"val_3"] # Subset the outer index level that meet val_1, val_2, val_3; notice that the initial and final values are both included, compared to slicing a list
# Special slicing feature for dates
df.loc["2020-01-27":"2022-03-09"]
df.loc["2020":"2022"]
df.loc[("val_1_for_col_1", "val_1_for_col_2"):("val_3_for_col_1", "val_3_for_col_2")] # Subset the outer index level that meet val_1_for_col_1, val_2_for_col_1, val_3_for_col_1, and then subset the inner index level that meet val_1_for_col_2, val_2_for_col_2, val_3_for_col_2

# Slice columns
df.loc[:, "col_name_1":"col_name_3"] # Select columns beginning from col_name_1 to col_name_3, and keep all rows

# Slice rows and columns at the same time
df.loc[("val_1_for_col_1", "val_1_for_col_2", "val_1_for_col_3"):("val_3_for_col_1", "val_3_for_col_2", "val_3_for_col_3"), "col_name_1":"col_name_3"] 

# Slicing and subsetting using iloc method, similar to slicing lists
# Slice lists
list_1[1:6] # Select the 2nd to 5th items in a list
list_1[:6] # Select from the beginning to the 5th item in a list
list_1[:] # Return the whole list

# Subset the DataFrame by row and column numbers
df.iloc[1:6, 1:6] # Select the 2nd to 5th rows and the 2nd to 5th columns
