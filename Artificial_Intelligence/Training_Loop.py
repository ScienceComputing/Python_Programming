# https://pytorch.org/docs/stable/generated/torch.optim.Adam.html

# A regression problem
from torch.utils.data import TensorDataset 
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import torch.optim as optim

num_epochs = 10

features = torch.tensor([[3.1, 2.2, 4.5, 1.3],
                         [1.9, 5.2, 2.7, 3.8],
                         [4.4, 0.8, 3.0, 2.1],
                         [2.5, 4.7, 1.6, 5.4]])

target = torch.tensor([[5.6], [3.2], [4.8], [2.9]])

dataset = TensorDataset(torch.tensor(features).float(), torch.tensor(target).float())
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

model = nn.Sequential(nn.Linear(4, 3, bias=True),
                      nn.ReLU(),
                      nn.Linear(3, 2, bias=True),
                      nn.ReLU(),
                      nn.Linear(2, 1, bias=True))

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(num_epochs):
    for data in dataloader:
        optimizer.zero_grad()
        inputs, labels = data
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

print("Final Loss:", loss.item())
