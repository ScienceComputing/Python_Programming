# Calculate the mean value of 5 columns in each row
mean_row = df[['Column1', 'Column2', 'Column3', 'Column4', 'Column5']].mean(axis=1) # Return a pandas series
mean_row_2 = df[['Column1', 'Column2', 'Column3', 'Column4', 'Column5']].values.mean(axis=1) # Return a ndarray; a bit faster than the above approach

# Calculate the mean of each of the 5 columns across all rows
mean_col = df[['Column1', 'Column2', 'Column3', 'Column4', 'Column5']].mean(axis=0)
mean_col_2 = df[['Column1', 'Column2', 'Column3', 'Column4', 'Column5']].values.mean(axis=0)
