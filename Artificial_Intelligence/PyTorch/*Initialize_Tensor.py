# PyTorch uses the fundamental data structure tensors (essentially arrays) to encode the inputs and outputs of a model, and the model’s parameters
# Tensors serve as multi-dimensional representations of their individual elements
import torch
import numpy as np

# Initilize a tensor 
# Method 1: initialization from a list
ori_data = [[5, 1, 0],[2, 0, 0]]
tensor_data = torch.tensor(ori_data)
# tensor([[5, 1, 0],
#         [2, 0, 0]])

# Access the tensor attributes
tensor_data.shape # torch.Size([2, 3])
tensor_data.dtype # torch.int64
tensor_data.device # device(type='cpu'); GPU boosts parallel computing capabilities

# Method 2: initialization from a numpy array
ori_data = np.array([[5, 1, 0],[2, 0, 0]])
tensor_data = torch.from_numpy(ori_data)

# Method 3: initialization from another tensor
ori_data = torch.tensor([[5, 1, 0],[2, 0, 0]])
tensor_data = torch.ones_like(ori_data)
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
