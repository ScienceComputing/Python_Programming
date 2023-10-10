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


# Count values in a particular column specified by the user
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

langs_count = count_entries(news_df, 'lang')
print(langs_count) # Print the number of news expressed per language


# Incorporate the error handling if the users specify the columns not in the dataframe
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

count_entries(news_df, 'lang_1')

# Count values in any arbitrary number of columns specified by the user
def count_entries_2(df, *args):
    """Return a dictionary with counts of occurrences as value for each key."""
    
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
                
    # Return the cols_count dictionary
    return cols_count

multi_col_count = count_entries_2(df, 'lang', 'source')
print(multi_col_count)
