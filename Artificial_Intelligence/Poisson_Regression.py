import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from sklearn.linear_model import PoissonRegressor, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Simulate the X and Y
np.random.seed(0)
n = 100 
beta_true = 9.0
X = np.random.normal(3, 1, n)
theta_true = np.exp(beta_true * X)
Y = np.random.poisson(theta_true)

# Make the scatter plot on the data
plt.scatter(X, Y, label="Simulated Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simulated Data")
plt.legend()
plt.show()

# Prepare the data
X = X.reshape(-1, 1)  # Reshape X for model fitting
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=899)

# Fit the Poisson Regression Model
poisson_model = PoissonRegressor()
poisson_model.fit(X_train, Y_train)
Y_pred_poisson = poisson_model.predict(X_test)

# Fit the Ridge Regularized Model with different lambdas
lambdas = list(np.arange(0, 500+0.01, 0.01))
ridge_models = {}
mse_scores = []

for lambda_val in lambdas:
    ridge_model = Ridge(alpha=lambda_val)
    ridge_model.fit(X_train, Y_train)
    Y_pred_ridge = ridge_model.predict(X_test)
    ridge_models[lambda_val] = ridge_model
    mse = mean_squared_error(Y_test, Y_pred_ridge)
    mse_scores.append(mse)

# Visualize the model performance with different lambdas
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(X_test, Y_test, label="True Data", alpha=0.5)
plt.plot(X_test, Y_pred_poisson, label="Poisson Regression", color='orange')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Poisson Regression vs. True Data")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(lambdas, mse_scores, marker='o')
plt.xlabel("Lambda (Regularization Strength)")
plt.ylabel("Mean Squared Error")
plt.title("Regularization (Ridge) Performance")
plt.xscale('log')
plt.show()
