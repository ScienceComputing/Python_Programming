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

X = torch.FloatTensor(X)
y = torch.FloatTensor(y)
X_train, X_validate, X_test = X[:n_train], X[n_train:n_train+n_validate], X[n_train+n_validate:]
y_train, y_validate, y_test = y[:n_train], y[n_train:n_train+n_validate], y[n_train+n_validate:]
train_data = TensorDataset(X_train, y_train)
validate_data = TensorDataset(X_validate, y_validate)
test_data = TensorDataset(X_test, y_test)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
validate_loader = DataLoader(validate_data, batch_size=32, shuffle=False)
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)


class PoissonRegression(nn.Module):
    def __init__(self, input_size):
        super(PoissonRegression, self).__init__()
        self.linear = nn.Linear(input_size, 1)

    def forward(self, x):
        return torch.exp(self.linear(x))

model = PoissonRegression(n_inputs)

def poisson_loss(output, target):
    return torch.mean(output - target * torch.log(output))

optimizer = optim.Adam(model.parameters(), lr=0.001)

n_epochs = 100
for epoch in range(n_epochs):
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()
        output = model(batch_X)
        loss = poisson_loss(output, batch_y)
        loss.backward()
        optimizer.step()
    
    with torch.no_grad():
        total_loss = 0
        for val_X, val_y in validate_loader:
            val_output = model(val_X)
            total_loss += poisson_loss(val_output, val_y)
        print(f"Epoch {epoch+1}/{n_epochs}, Validation Loss: {total_loss/len(validate_loader):.4f}")

model.eval()
with torch.no_grad():
    test_loss = 0
    for test_X, test_y in test_loader:
        test_output = model(test_X)
        test_loss += poisson_loss(test_output, test_y)
    print(f"Test Loss: {test_loss/len(test_loader):.4f}")

# Visualize the predicted distribution
model.eval()
with torch.no_grad():
    predicted_y = model(X_test).numpy()
    
plt.figure(figsize=(10, 5))
plt.hist(y_test.numpy(), bins=np.linspace(0,100, 101), alpha=0.5, label='Actual')
plt.hist(predicted_y, bins=np.linspace(0,100, 101), alpha=0.5, label='Predicted')
plt.legend()
plt.show()
