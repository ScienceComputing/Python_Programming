# PyTorch uses tensors to encode the inputs and outputs of a model, and the model’s parameters
import torch
import numpy as np

# Initilize a tensor 
# Method 1: initialization from data
original_data = [[5, 1, 0],[2, 0, 0]]
tensor_data = torch.tensor(original_data)

# Method 2: initialization from a numpy array
original_data = np.array([[5, 1, 0],[2, 0, 0]])
tensor_data = torch.from_numpy(original_data)

# Method 3: initialization from another tensor
original_data = torch.tensor([[5, 1, 0],[2, 0, 0]])
tensor_data = torch.ones_like(original_data)
print(f"Ones tensor - \n {tensor_data} \n")

tensor_data_2 = torch.rand_like(original_data, dtype=torch.float)
print(f"Random number tensor - \n {tensor_data_2} \n")

# Method 4: initialization with random or constant values
shape = (5,6,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"random tensor - \n {rand_tensor} \n")
print(f"Ones tensor - \n {ones_tensor} \n")
print(f"Zeros tensor - \n {zeros_tensor}")
