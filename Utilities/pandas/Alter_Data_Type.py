df['feature'] = df.feature.astype(float)

df.drug_class.unique() # View the unique values in the drug_class column
df['drug_class'] = df.drug_class.astype('category')

df['diagnosis_time'] = pd.to_datetime(df.diagnosis_time) # Convert diagnosis_time to datetime
df.info() # Inspect the cleaned dataset
