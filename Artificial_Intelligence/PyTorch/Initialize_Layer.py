# Implement a neural network with one linear layer
import torch.nn as nn
layer = nn.Linear(in_features=9, out_features=27)
print(layer.weight.min(), layer.weight.max())
