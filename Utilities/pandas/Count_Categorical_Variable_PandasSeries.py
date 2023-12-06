# Set up the environment
import pandas as pd
# Import news data as DataFrame: df
news_df = pd.read_csv("news.csv")  
# Initialize an empty dictionary: langs_count
langs_count = {}
# Extract column from DataFrame: col
langs_col = news_df['lang']
type(langs_col) # pandas.core.series.Series

# Method 1:
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

# Method 2:
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

# Method 2.1:
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

# Method 2.2:
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
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

count_entries(news_df, 'lang_1')

# !Method 3:
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

df = adata.obs
sm_name_count = count_entries_2(df, 'sm_name')
print(sm_name_count)
sm_cluster_3_count = count_entries_2(df, 'sm_cluster_3')
print(sm_cluster_3_count)

# Method 4: if the given dataframe is very large
counts_dict={}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('news.csv',chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)

# Method 5: ask users to freely choose the input data file, chunk size, and target column
def count_entries_3(csv_file, c_size, colname):
    """Return a dictionary with counts of occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict


result_counts = count_entries_3('news.csv', 100, 'lang')
print(result_counts)
