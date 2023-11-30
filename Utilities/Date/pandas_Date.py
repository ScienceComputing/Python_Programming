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
eb['duration'].median()
eb['duration'].mode()
eb['duration'].min()
eb['duration'].max()
eb['duration'].var()
eb['duration'].std()
eb['duration'].sum()
eb['duration'].quantile()
eb['product type'].value_counts()
eb['product type'].value_counts()/len(eb)
eb['duration in seconds'] = eb['duration'].dt.total_seconds()
eb.groupby('product type')['duration in seconds'].mean()

# Estimate the average duration in seconds grouped by month
eb.resample('M', on = 'start date')['duration in seconds'].mean()
# Estimate the size of each group
eb.groupby('product type').size() 
# Retrieve the first row of each group
eb.groupby('product type').first()

# Visualize the average duration in seconds grouped by month in a line plot
eb.resample('M', on = 'start date')['duration in seconds'].mean().plot()
# Visualize the average duration in seconds grouped by day in a line plot
eb.resample('D', on = 'start date')['duration in seconds'].mean().plot()

