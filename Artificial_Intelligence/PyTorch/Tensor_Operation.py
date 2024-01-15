import torch

# Element-wise addition
data_1 = torch.tensor([[1, 5, 6], [2, 6, 9]])
data_2 = torch.tensor([[0, 1, 1], [3, 3, 2]])
data_1 + data_2
# tensor([[ 1,  6,  7],
#         [ 5,  9, 11]])

# Element-wise multiplication
data_1 * data_2
# tensor([[ 0,  5,  6],
#         [ 6, 18, 18]])
