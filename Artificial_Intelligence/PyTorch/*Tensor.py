# PyTorch uses the fundamental data structure tensors (essentially arrays) to encode the inputs and outputs of a model, and the model’s parameters
# Tensors serve as multi-dimensional representations of their individual elements
# pip3 install torch torchvision
import torch
import numpy as np

print('*****************************************')
print('Initilize a tensor')
print('*****************************************\n')
# Method 1: initialization from a list
ori_data = [[5, 1, 0],[2, 0, 0]]
tensor_data = torch.tensor(ori_data)
# tensor([[5, 1, 0],
#         [2, 0, 0]])

# Access the tensor attributes
tensor_data.shape # torch.Size([2, 3])
tensor_data.dtype # torch.int64
tensor_data.device # device(type='cpu'); GPU boosts parallel computing capabilities; faster training time; better computing performance

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


print('*****************************************')
print('Operate a tensor')
print('*****************************************\n')

# Most operations we can do with NumPy arrays can also be done with PyTorch tensors
# Element-wise addition for compatile shapes
data_1 = torch.tensor([[1, 5, 6], [2, 6, 9]])
data_2 = torch.tensor([[0, 1, 1], [3, 3, 2]])
data_1 + data_2
# tensor([[ 1,  6,  7],
#         [ 5,  9, 11]])

data_1 = torch.tensor([[1, 5, 6], [2, 6, 9]])
data_2 = torch.tensor([[0, 1], [3, 3]])
data_1 + data_2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# RuntimeError: The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 1

# Element-wise multiplication
data_1 = torch.tensor([[1, 5, 6], [2, 6, 9]])
data_2 = torch.tensor([[0, 1, 1], [3, 3, 2]])
data_1 * data_2
# tensor([[ 0,  5,  6],
#         [ 6, 18, 18]])

# Transposition
data_1.T

# Matrix multiplication
data_1 = torch.tensor([[1, 5, 6], [2, 6, 9]])
data_2_t = torch.tensor([[0, 1, 1], [3, 3, 2]]).T
data_1 @ data_2_t

# Concatenation
# Concatenate along the rows
torch.cat((data_1, data_2), dim=0)
# tensor([[1, 5, 6],
#         [2, 6, 9],
#         [0, 1, 1],
#         [3, 3, 2]])

# Concatenate along the columns
torch.cat((data_1, data_2), dim=1)
# tensor([[1, 5, 6, 0, 1, 1],
#         [2, 6, 9, 3, 3, 2]])

