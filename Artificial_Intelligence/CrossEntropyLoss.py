# Case 1:
from sklearn.metrics import log_loss
true_label = ["ginger", "rose", "rose", "ginger"]
pred_prob = [[.1, .9], [.8, .2], [.9, .1], [.05, .95]]
log_loss(true_label, pred_prob)
# 2.3025850929940455

log_loss(["spam", "ham", "ham", "spam"], [[.1, .9], [.8, .2], [.9, .1], [.05, .95]])
# 0.1212894692543532 # TD ?


# Case 2:
import torch
import torch.nn as nn

def compute_cross_entropy_loss_and_backpropagate():
    # Create a CrossEntropyLoss instance
    loss = nn.CrossEntropyLoss()
    # Create random input data (690 samples, 2 classes)
    input = torch.randn(690, 2, requires_grad=True)
    # Create a random target tensor (690 samples with class indices)
    target = torch.empty(690, dtype=torch.long).random_(2)
    # Calculate the loss between the input and target
    output = loss(input, target)
    # Perform backpropagation to compute gradients
    output.backward()
    return output, input.grad

# Call the function to calculate the loss and gradients
loss_value, gradients = compute_cross_entropy_loss_and_backpropagate()

# Print the loss value and gradients
print("Loss Value:", loss_value.item())
print("Gradients:\n", gradients)
