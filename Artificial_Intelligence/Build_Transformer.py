pip3 install torch torchvision torchaudio

# A weighting scheme enables a transformer model to give varying degrees of attention to different segments of the input when generating an output.
# Set up the working environment
pip3 install torch torchvision torchaudio

# Import the libraries and modules
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import math
import copy

# Define Multi-head Attention, Position-Wise Feed-Forward Networks, Positional Encoding
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()

        # Check if d_model is divisible by num_heads
        if d_model % num_heads != 0:
            raise ValueError("d_model must be divisible by num_heads")

        # Initialize dimensions
        self.d_model = d_model             # Model's dimension
        self.num_heads = num_heads         # Number of attention heads
        self.d_k = d_model // num_heads    # Dimension of each head's key, query, and value

        # Build linear layers for transforming inputs
        self.W_q = nn.Linear(d_model, d_model)  # Query transformation
        self.W_k = nn.Linear(d_model, d_model)  # Key transformation
        self.W_v = nn.Linear(d_model, d_model)  # Value transformation
        self.W_o = nn.Linear(d_model, d_model)  # Output transformation
