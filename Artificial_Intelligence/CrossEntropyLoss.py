# Case 1:
from sklearn.metrics import log_loss
true_label = ["ginger", "rose", "rose", "ginger"]
pred_prob = [[.1, .9], [.8, .2], [.9, .1], [.05, .95]]
log_loss(true_label, pred_prob)
# 2.3025850929940455

log_loss(["spam", "ham", "ham", "spam"], [[.1, .9], [.8, .2], [.9, .1], [.05, .95]])
# 0.1212894692543532 # TD ?

# Case 2.1: 
import torch
import torch.nn as nn
import torch.nn.functional as F

score = torch.tensor([[10, 2, -3, 6, 9, 19]]) # Predictions for 6 classes per subject 
one_hot_label = F.one_hot(torch.tensor(0), num_classes=6).unsqueeze(0)
one_hot_label 
loss = nn.CrossEntropyLoss()
loss_value = loss(score.double(), one_hot_label.double())
print(loss_value) 

# Case 2.2:
import torch
import torch.nn as nn

def compute_cross_entropy_loss_and_backpropagate(score, one_hot_label):
    loss = nn.CrossEntropyLoss()
    output = loss(score, one_hot_label)
    output.backward()
    return output, score.grad

# Create random input data (690 samples, 3 classes)
input = torch.randn(690, 3, requires_grad=True)
# Create a random target tensor (690 samples with 3 class indices)
target = torch.empty(690, dtype=torch.long).random_(3)

loss_value, gradients = compute_cross_entropy_loss_and_backpropagate(input, target)

print("Loss Value:", loss_value.item())
print("Gradients:\n", gradients)


