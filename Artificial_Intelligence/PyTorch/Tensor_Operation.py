# pip3 install torch torchvision
import torch

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

# Matrix multiplication

# Concatenation
