# Implement a neural network with one linear layer
import torch.nn as nn
layer = nn.Linear(in_features=9, out_features=27)
print(layer.weight.min(), layer.weight.max())

# Initialize layer weights with the uniform distribution
# To make sure the outputs of our layer stay small, it's important to the layer weights on the lower side
layer = nn.Linear(64, 128)
nn.init.uniform_(layer.weight) 
print(layer.weight.min(), layer.weight.max())
