# Topic: missing values (NaN)
# Motivation: some python functions ignore missing data by default, and some functions cannot handle the missing data

# Detect the missing values
df.isna() # Return a Boolean for every single element in the dataset
df.isna().any() # Return a Boolean for every column in the dataset
df.isna().sum() # Return a count for missing values for every column in the dataset

# Visualize the missing values across different variables using the bar plot 
Import matplotlib.pyplot as plt
df.isna().sum().plot(kind="bar")
plot.show()

# Remove the missing values
df.dropna() # Remove the rows that contain missing values

# Replace the missing values with 0 
df.fillna(0) # Notice the distribution of variables with the missing values may change after replacing the missing values with 0
df["numerical_var_before_replace"].hist(bins=20)
plt.show()
df["numerical_var_after_replace"].hist(bins=20)
plt.show()

# Replace originally coded missing values with NaN (not a number) in the disease column
df.disease.replace(['Unknown', 'Unk', 'UNK', 'None', 'none', 'missing', 'No', 'no'], np.nan, inplace=True)
