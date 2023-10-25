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

# Relationships between numeric variables (mileage/tax/mpg) and the target variable (price)
# Use the correlation heatmap to study the linear relationships between two continous variables
numeric = df[['price','mileage','tax','mpg']]
sns.heatmap(numeric.corr(),annot=True).set(title='The Correlation Heatmap between Numeric Variables');

# Use the scatterplot to study the **non-linear** relationships between two continous variables
fig, axes = plt.subplots(1,3,figsize=(15,5))
sns.scatterplot(y=df['price'],x=df['mpg'],color='gray',ax=axes[0]).set(title='The Scatterplot between Price and Mpg')
sns.scatterplot(y=df['price'],x=df['tax'],color='gray',ax=axes[1]).set(title='The Scatterplot between Price and Tax')
sns.scatterplot(y=df['price'],x=df['mileage'],color='gray',ax=axes[2]).set(title='The Scatterplot between Price and Mileage');
# Since there exist **clusters** in the scatterplot between price and tax, we'are going to create an **ordinal variable** from the tax variable.

# Characteristics of categorical variables - **Year**, **Engine Size**, Model, Transmission, fuelType
# Use the barplot to study the count per categorical level
fig, axes = plt.subplots(1,2,figsize=(15,5))
sns.countplot(x=df['year'], color='gray',ax=axes[0]).set(title='Count of Cars Sold per Manufacture Year')
sns.countplot(x=df['engineSize'],color='gray',ax=axes[1]).set(title='Count of Cars Sold per EngineSize')
axes[0].tick_params(axis='x', labelrotation=45)
axes[1].tick_params(axis='x', labelrotation=45);

fig, axes = plt.subplots(1,3,figsize=(15,5))
sns.countplot(x=df['model'],color='gray',ax=axes[0]).set(title='Count of Cars Sold per Model')
sns.countplot(x=df['transmission'],color='gray',ax=axes[1]).set(title='Count of Cars Sold per Transmission')
sns.countplot(x=df['fuelType'],color='gray',ax=axes[2]).set(title='Count of Cars Sold per Fuel Type')
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=90);

# Use the boxplot to examine how continuous Price changes along with the increasing categorical Year or Engine Size
fig, axes = plt.subplots(1,2,figsize=(20,5))
sns.boxplot(data=df, x='year',y='price',color='gray', ax=axes[0]).set(title='The Relationship Between Year and Price')
sns.boxplot(data=df, x='engineSize',y='price',color='gray', ax=axes[1]).set(title='The Distribution of Price by Engine Size')
for ax in fig.axes:
    plt.sca(ax)
    plt.xticks(rotation=90);

# Optional: use the scatterplot to show the relationship between Price, Year, and Engine Size in one visual
sns.scatterplot(data=df, x='year',y='price',color='gray', hue='engineSize').set(title='The Relationship Between Manufacture Year, Price and Engine Size');
