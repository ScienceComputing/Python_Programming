pd.read_csv()
pd.read_excel()
pd.read_json()
pd.read_clipboard()

# Get a glimpse of 20 values randomly selected in a column named disease
df.disease.sample(n=20)

# Get a glimpse of 20 values randomly selected of the disease column that are not 'Norovirus'
df[df.disease != 'Norovirus'].disease.sample(n=20)
