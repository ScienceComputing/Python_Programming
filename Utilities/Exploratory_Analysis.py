import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Make histograms for numerical variables
df.hist(figsize=(10,10), bins=50)
plt.show()

# View the numeric variables
df.describe()

# View the non-numeric variables
df.describe(exclude=[np.number])

# View a particular variable
df.age.describe()

# View the unique values in a character variable
df.physician_language.unique()

# Capitalize each language
df['physician_language'] = df.physician_language.str.capitalize()
df.physician_language.unique()
