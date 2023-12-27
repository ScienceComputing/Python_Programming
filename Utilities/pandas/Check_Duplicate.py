# Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html
# keep: {‘first’, ‘last’, False}, default ‘first’ - Determines which duplicates (if any) to mark.
# first : Mark duplicates as True *except for the first occurrence.
# last : Mark duplicates as True *except for the last occurrence.
# False : Mark all duplicates as True.


# Seach for duplicate rows
df.duplicated().sum()

# Search for duplicates in specified columns
audible.duplicated(subset=['name', 'ID']).sum()

# Examine the duplicated rows keeping the duplicates and ordered by the ID column
df[df.duplicated(subset=['name', 'ID'], keep=False)].sort_values(by='ID')

# Drop duplicated rows while keep the last record within a duplicated chunk
df.drop_duplicates(subset=['name', 'ID'], keep='last', inplace=True)
df.duplicated(subset=['name', 'ID']).sum()
