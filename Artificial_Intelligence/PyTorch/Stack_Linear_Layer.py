import torch
import torch.nn as nn

DE_data = np.loadtxt("DE_result.csv", delimiter=",") 
input_tensor = torch.from_numpy(DE_data)

pred_model = nn.Sequential(
    nn.Linear(in_features=input_tensor.shape[1], out_features=100), 
    nn.Linear(in_features=100, out_features=70), 
    nn.Linear(in_features=70, out_features=30)  # 30 predictions for the phenotype classification
)

pred_result = pred_model(input_tensor)
print(pred_result)
