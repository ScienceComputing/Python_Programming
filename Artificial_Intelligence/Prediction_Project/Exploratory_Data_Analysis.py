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

# Target varibale - price
# As we aim to forecast the price, our target variable is the 'price.' 
# Analyzing the histogram on the left, we observe an extended right tail. 
# Consequently, we use a **logarithmic transformation** on the 'price' variable [target variable], resulting in a distribution resembling a **normal distribution**, as depicted in the right histogram.
fig, axes = plt.subplots(1,2,figsize=(15,5))
sns.histplot(df['price'],color='gray',ax=axes[0]).set(title='The Distribution of Price')
sns.histplot(df['price'],log_scale=True,color='gray',ax=axes[1]).set(title='The Distribution of Log-Transformed Price');

# Relationships between numeric variables (mileage/tax/mpg) and the target variable
# Study the linear relationships between two continous variables
numeric = df[['price','mileage','tax','mpg']]
sns.heatmap(numeric.corr(),annot=True).set(title='The Correlation Heatmap between Numeric Variables');

# Study the **non-linear** relationships between two continous variables
fig, axes = plt.subplots(1,3,figsize=(15,5))
sns.scatterplot(y=df['price'],x=df['mpg'],color='gray',ax=axes[0]).set(title='The Scatterplot between Price and Mpg')
sns.scatterplot(y=df['price'],x=df['tax'],color='gray',ax=axes[1]).set(title='The Scatterplot between Price and Tax')
sns.scatterplot(y=df['price'],x=df['mileage'],color='gray',ax=axes[2]).set(title='The Scatterplot between Price and Mileage');
