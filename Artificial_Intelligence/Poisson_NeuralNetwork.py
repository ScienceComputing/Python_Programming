import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from torch.distributions import Poisson
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Generate some data from the true Poisson model
# $$
# y_i \sim \text{Poisson}(\exp(0.2x_1^2 + 0.8*x_2x_3 + 3\sin(x_4) + 2\log(\mid x_5 \mid)) + 18) \, .
# $$
n_train = 1000
n_validate = 500
n_test = 5000
n_inputs = 5
X = np.random.normal(size=(n_train+n_validate+n_test, n_inputs))
y = np.random.poisson(np.exp(0.2*X[:,0]**2 + 0.8*X[:,1]*X[:,2] + 3 * np.sin(X[:,3]) + 2*np.log(np.abs(X[:,4]))) + 18)


# Visualize the distribution of all the data
plt.hist(y, bins=100)

# Visualize the distribution of the partial data from 0 to 100
plt.hist(y, bins=np.linspace(0,100, 101))
