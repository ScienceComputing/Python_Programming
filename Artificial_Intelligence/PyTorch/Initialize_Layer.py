# Implement a neural network with one linear layer
import torch.nn as nn
layer = nn.Linear(in_features=9, out_features=27)
print(layer.weight.min(), layer.weight.max())

# Initialize weights of one layer with the uniform distribution
# To make sure the outputs of our layer stay small, it's important to the layer weights on the lower side
layer = nn.Linear(64, 128)
nn.init.uniform_(layer.weight) 
print(layer.weight.min(), layer.weight.max())

# Initialize weights of two layers with the uniform distribution
layer_0 = nn.Linear(3, 9)
layer_1 = nn.Linear(9, 27)
nn.init.uniform_(layer_0.weight)
nn.init.uniform_(layer_1.weight)
model = nn.Sequential(layer_0, layer_1)
for name, param in model.named_parameters():
  print(name, param)

# Transfer the weights from the first model to train the second model
import torch
layer = nn.Linear(in_features=9, out_features=27)
torch.save(layer, 'layer.pt')

layer_2 = torch.load('layer.pt')

# Only train the last layer; freeze the first two layers
model = nn.Sequential(
	nn.Linear(in_features=3, out_features=9, bias=True),
	nn.Linear(in_features=9, out_features=27, bias=True),
	nn.Linear(in_features=27, out_features=81, bias=True))

for name, param in model.named_parameters():
    if name in ['0.weight', '0.bias', '1.weight', '1.bias']:
        param.requires_grad = False

