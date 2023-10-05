# Import pandas
import pandas as pd

# Import news data as DataFrame: df
news_df = pd.read_csv("news.csv")  

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
langs_col = news_df['lang']
type(langs_col)
# pandas.core.series.Series

# Iterate over lang column in DataFrame
for entry in langs_col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count.update({entry: 1}) #!

# Print the populated dictionary
print(langs_count)

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of occurrences as value for each key."""

    # Initialize an empty dictionary: count
    count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If the entry is in the dictionary count, add 1
        if entry in count.keys():
            count[entry] += 1
        # Else add the entry to count, set the value to 1
        else:
            count.update({entry: 1})

    # Return the count dictionary
    return count

# Call count_entries(): result
langs_count = count_entries(news_df, 'lang')

# Print the number of news expressed per language
print(langs_count)
