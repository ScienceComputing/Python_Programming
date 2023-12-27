hours = df['diagnosis_time'].str.extract('(\d+) hr').fillna(0).astype(int) # fill NaN with 0
mins = df['diagnosis_time'].str.extract('(\d+) min').fillna(0).astype(int)
df['diagnosis_time_mins'] = hours * 60 + mins
df[['time_mins']]
