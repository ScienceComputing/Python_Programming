import pandas as pd
df = pd.read_csv('RNA_velocity.csv')

# Select the columns whose names start with 'Vol'
df.filter(regex='^Vol')
