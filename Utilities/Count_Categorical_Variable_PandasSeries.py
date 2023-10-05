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
        langs_count.update({entry: 1})

# Print the populated dictionary
print(langs_count)
