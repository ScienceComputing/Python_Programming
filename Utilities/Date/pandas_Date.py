"""
Parse the date columns
"""
import pandas as pd

eb = pd.read_csv('energy_bar_sales.csv', 
                 parse_dates = ['start date', 'end date'])

print(eb.iloc[0]) # Retrieve the 0th row

# Alternative approach
eb['start date'] = pd.to_datetime(eb['start date'], format = '%Y-%m-%d %H:%M:%S')

"""
Parse the date columns in a particular timezone
"""
eb['start date'] = eb['start date'].dt.tz_localize('America/New_York', ambiguous='NaT')
eb['end date'] = eb['end date'].dt.tz_localize('America/New_York', ambiguous='NaT')
eb['duration'] = eb['end date'] - eb['start date'] 
eb['duration'].dt.total_seconds().min() # No negative value

"""
Transform the duration into seconds
"""
eb = pd.read_csv('energy_bar_sales.csv', 
                 parse_dates = ['start date', 'end date'])
eb['duration'] = eb['end date'] - eb['start date'] # Naive date, not timezone-aware
print(eb['duration'].head(3))
eb['duration'].dt.total_seconds().head(3)
# Get typical datetime methods within the namespace `.dt`.

"""
Find the smallest duration in seconds
"""
eb['duration'].dt.total_seconds().min()

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
# Estimate the average duration in seconds grouped by product type and month
eb.groupby('product type').resample('M', on = 'Start date').mean()

# Visualize the average duration in seconds grouped by month in a line plot
eb.resample('M', on = 'start date')['duration in seconds'].mean().plot()
# Visualize the average duration in seconds grouped by day in a line plot
eb.resample('D', on = 'start date')['duration in seconds'].mean().plot()
# Visualize the size of each month in a line plot
eb.resample('M', on = 'start date').size().plot()

"""
Get year and weekdays
"""
eb['start date'].dt.year
eb['start date'].dt.day_name()
