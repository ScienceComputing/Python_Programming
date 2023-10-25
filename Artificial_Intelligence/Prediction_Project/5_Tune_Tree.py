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

# Tune the maximum depth of the tree for Decision Tree Regression Model
train_score = []
test_score = []
rmse_score = []
max_score = 0
max_pair = (0,0)
min_pair_rmse = (0,float('inf'))

for i in range(1,50):
    tree = DecisionTreeRegressor(max_depth=i,random_state=99)
    tree.fit(X_train,y_train)
    y_pred = tree.predict(X_test)
    # Calculate training R2 and append it to the train_score list
    train_score.append(tree.score(X_train,y_train))
    # Calculate test R2 and append it to the test_score list
    temp = r2_score(y_test,y_pred)
    test_score.append(temp)
    test_pair = (i,temp)
    # Calculate RMSE and append it to the rmse_scores list
    rmse = np.sqrt(mean_squared_error(np.exp(y_pred), np.exp(y_test)))
    rmse_score.append(rmse)
    rmse_pair = (i, rmse)
    
    # Check for the maximum R2 
    if test_pair[1] > max_pair[1]:
        max_pair = test_pair

    # Check for the minimum RMSE 
    if rmse_pair[1] < min_pair_rmse[1]:
        min_pair_rmse = rmse_pair

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# Plot max_depth vs. training and testing R^2 scores
ax1.plot(np.arange(1, 50), train_score, label="Training R^2", color='lightcoral')
ax1.plot(np.arange(1, 50), test_score, label="Testing R^2", color='lime')
ax1.set_xlabel('max_depth')
ax1.set_ylabel('R^2')
ax1.legend()

# Plot max_depth vs. RMSE
ax2.plot(np.arange(1, 50), rmse_score, label="RMSE", color='blue')
ax2.set_xlabel('max_depth')
ax2.set_ylabel('RMSE')
ax2.legend()

print(f'Best max_depth is: {max_pair[0]} \nTesting R^2 is: {max_pair[1]}')
print(f'Best max_depth (RMSE) is: {min_pair_rmse[0]}\nMinimum RMSE is: {min_pair_rmse[1]}')

# Best max_depth is: 10 
# Testing R^2 is: 0.9444455033877253
# Best max_depth (RMSE) is: 10
# Minimum RMSE is: 1483.2072295396115

# TD: AI in Medicine: tune more parameters

# Use the barplot to show the feature importance
importance = tree.feature_importances_ # Return an array
new_col_names = ['Year','Transmission', 'Fuel Type','Engine Size','Tax','Model','Mileage']
f_importance = {}
for i in range(len(features)):
     f_importance[new_col_names[i]] = importance[i]
        
plt.bar(f_importance.keys(),f_importance.values(),alpha=0.5,color='gray')
plt.xticks(rotation=45)
plt.title('Feature Importance in Decision Tree Regression Model');
