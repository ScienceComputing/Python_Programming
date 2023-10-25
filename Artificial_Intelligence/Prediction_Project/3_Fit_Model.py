# Predicting prices presents a regression challenge within the realm of machine learning. 
# For the model fitting, We've opted for the Linear Regression model due to the observable moderate to strong associations between certain features and the target variable. 
# As for the alternative model, we've selected the Decision Tree regression model, primarily for its easy interpretability independent of outliers.
# For the model evaluation, we will use both R squared and RMSE (Root Mean Squared Error) to gauge the model's performance. 
# R squared assesses how effectively the model uses the features to model the dependent variables.
# On the other hand, RMSE quantifies the extent to which the predicted outcomes differ from the actual values.

# Prepare data to fit the model
df['log_price'] = np.log(df['price'])
