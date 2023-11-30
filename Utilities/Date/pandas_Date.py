# Parse the date columns
import pandas as pd

eb = pd.read_csv('energy_bar_sales.csv', 
                 parse_dates = ['start date', 'end date'])

print(eb.iloc[0]) # Retrieve the 0th row
