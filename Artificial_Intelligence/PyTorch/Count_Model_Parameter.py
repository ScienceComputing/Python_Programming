# The count of parameters is important in gauging a model's capacity and intricacy. 
# It's essential to monitor the parameter count in each layer of the model to address overfitting or underfitting issues. 
# To overcome overfitting or underfitting, one approach is to fine-tune the number of parameters in each layer. 

import torch
import torch.nn as nn

new_model = nn.Sequential(
    nn.Linear(10, 8),
    nn.ReLU(),
    nn.Linear(8, 6),
    nn.ReLU(),
    nn.Linear(6, 4),
    nn.ReLU(),
    nn.Linear(4, 3),
    nn.ReLU(),
    nn.Linear(3, 2),
    nn.ReLU(),
    nn.Linear(2, 1)
)

total_params = 0

for param in new_model.parameters():
    total_params += param.numel()

print(f"Total number of parameters in the new model: {total_params}")
