# Calculate the mean value of 5 columns in each row
mean_row = df[['Column1', 'Column2', 'Column3', 'Column4', 'Column5']].mean(axis=1)

# Calculate the mean of each of the 5 columns in all rows
mean_col = df[['Column1', 'Column2', 'Column3', 'Column4', 'Column5']].mean(axis=0)
