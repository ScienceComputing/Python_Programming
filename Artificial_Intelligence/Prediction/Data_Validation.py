import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import PowerTransformer
from sklearn.metrics import r2_score,mean_squared_error
plt.style.use('ggplot')

df = pd.read_csv('data/car_data.csv')
df.info()
df.head()

# Validate the variables
# Count the number of unique values in the selected column
df['model'].nunique()
df['engineSize'].nunique()
# Return an array containing all the unique values found in the selected column
df['year'].unique()
df['transmission'].unique()
df['fuelType'].unique()

# Search for any negative values in numeric variables
df.describe()
