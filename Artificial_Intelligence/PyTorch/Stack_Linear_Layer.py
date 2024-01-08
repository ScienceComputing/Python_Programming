# Reference: https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html

import torch
import torch.nn as nn

DE_data = np.loadtxt("DE_result.csv", delimiter=",", skiprows=1) 
input_tensor = torch.from_numpy(DE_data)

import numpy as np

pred_model = nn.Sequential(
    nn.Linear(in_features=input_tensor.shape[1], out_features=100), 
    nn.Linear(in_features=100, out_features=70), 
    nn.Linear(in_features=70, out_features=30), 
    nn.Linear(in_features=30, out_features=1),
    nn.Sigmoid()
)

pred_result = pred_model(input_tensor)
print(pred_result)

num_class = 6
pred_model_2 = nn.Sequential(
    nn.Linear(in_features=input_tensor.shape[1], out_features=100), 
    nn.Linear(in_features=100, out_features=70), 
    nn.Linear(in_features=70, out_features=30),
    nn.Linear(in_features=30, out_features=num_class), # predictions for the multi-class (6-class) phenotype classification 
    nn.Softmax(dim=-1)
)

pred_result_2 = pred_model_2(input_tensor)
print(pred_result_2)
