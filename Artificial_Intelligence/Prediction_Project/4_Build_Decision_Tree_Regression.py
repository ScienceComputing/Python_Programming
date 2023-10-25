# Set up the environment
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

# Build the tree model
tree = DecisionTreeRegressor(max_depth=12,min_samples_split=2,random_state=99)
tree.fit(X_train,y_train)
y_pred_2 = tree.predict(X_test)

# Use R-squared and RMSE to evaulate the model performance
d_r2 = tree.score(X_test, y_test)
print("Decision Tree Regressor R-squared: {}".format(d_r2))

d_mse = mean_squared_error(np.exp(y_pred_2), np.exp(y_test))
d_rmse = np.sqrt(d_mse)
print("Decision Tree Regressor RMSE: {}".format(d_rmse))
