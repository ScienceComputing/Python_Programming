"""
Parse the date columns
"""
import pandas as pd

eb = pd.read_csv('energy_bar_sales.csv', 
                 parse_dates = ['start date', 'end date'])

print(eb.iloc[0]) # Retrieve the 0th row

# Alternative approach
eb['start date'] = pd.to_datetime(eb['start date'], format = '%Y-%m-%d %H:%M:%S')

eb['duration'] = eb['end date'] - eb['start date']
print(eb['duration'].head(3))

"""
Transform the duration into seconds
"""
eb['duration'].dt.total_seconds().head(3)
# Get typical datetime methods within the namespace `.dt`.

"""
Summarize date time
"""
eb['duration'].mean()
