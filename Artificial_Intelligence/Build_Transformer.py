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

    def scaled_dot_product_attention(self, Q, K, V, mask=None):
        # Calculate attention scores
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)
        
        # Apply mask if provided (typically used for masking out certain elements, like padding tokens)
        if mask is not None:
            attn_scores = attn_scores.masked_fill(mask == 0, -1e9)
        
        # Use softmax to obtain attention probabilities
        attn_probs = torch.softmax(attn_scores, dim=-1)
        
        # Compute the Weighted Sum of Values
        output = torch.matmul(attn_probs, V)
        return output

    def split_heads(self, x):
        # Modify the input to accommodate multiple heads for the multi-head attention mechanism.
        batch_size, seq_length, d_model = x.size()
        return x.view(batch_size, seq_length, self.num_heads, self.d_k).transpose(1, 2)
    
    def combine_heads(self, x):
        # Reassemble the multiple heads to restore the original shape
        batch_size, _, seq_length, d_k = x.size()
        return x.transpose(1, 2).contiguous().view(batch_size, seq_length, self.d_model)
    
    def forward(self, Q, K, V, mask=None):
        # Build linear layers for transforming inputs and split heads
        Q = self.split_heads(self.W_q(Q))
        K = self.split_heads(self.W_k(K))
        V = self.split_heads(self.W_v(V))
        
        # Conduct scaled dot-product attention
        attn_output = self.scaled_dot_product_attention(Q, K, V, mask)
        
        # Reassemble the multiple heads to restore the original shape and build linear layers for transforming the output
        output = self.W_o(self.combine_heads(attn_output))
        return output
