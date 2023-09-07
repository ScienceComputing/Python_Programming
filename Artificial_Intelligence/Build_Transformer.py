# A weighting scheme enables a *transformer* model to give varying degrees of attention to different segments of the input when generating an output.

# Set up the working environment
pip3 install torch torchvision torchaudio

# Import the libraries and modules
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import math
import copy

# Define Multi-head Attention
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        """
        MultiHeadAttention class serves as a container for the multi-head attention mechanism, a frequent component in transformer models. 
        Its responsibilities include dividing the input into multiple attention heads, applying attention individually to each head, and subsequently amalgamating the outcomes. 
        This process enhances the model's capability to discern diverse relationships within the input data at varying levels of granularity, ultimately enhancing the model's expressiveness.
        d_model: dimensionality of the input
        num_heads: the number of attention heads to split the input into.
        """
        super(MultiHeadAttention, self).__init__()

        # Check if d_model is divisible by num_heads
        if d_model % num_heads != 0:
            raise ValueError("d_model must be divisible by num_heads")

        # Initialize dimensions
        self.d_model = d_model             # Model's dimension
        self.num_heads = num_heads         # Number of attention heads
        self.d_k = d_model // num_heads    # Dimension of each head's key, query, and value

        # Build linear layers for transforming inputs
        self.W_q = nn.Linear(d_model, d_model)  # Define the transformation weights for query
        self.W_k = nn.Linear(d_model, d_model)  # Define the transformation weights for key
        self.W_v = nn.Linear(d_model, d_model)  # Define the transformation weights for value
        self.W_o = nn.Linear(d_model, d_model)  # Define the transformation weights for output

    def scaled_dot_product_attention(self, Q, K, V, mask=None):
        # Calculate attention scores
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)
        
        # Apply mask if provided (typically used for masking out certain elements, like padding tokens)
        if mask is not None:
            attn_scores = attn_scores.masked_fill(mask == 0, -1e9)
        
        # Use softmax to convert the attention scores into attention probabilities that sum to 1
        attn_probs = torch.softmax(attn_scores, dim=-1)
        
        # Compute the output by multiplying the attention weights by the values (V)
        output = torch.matmul(attn_probs, V)
        return output

    def split_heads(self, x):
        # Reshape the input x into the shape (batch_size, num_heads, seq_length, d_k)
        # Process multiple attention heads concurrently
        batch_size, seq_length, d_model = x.size()
        return x.view(batch_size, seq_length, self.num_heads, self.d_k).transpose(1, 2)
    
    def combine_heads(self, x):
        # Combine the results back into a single tensor of shape (batch_size, seq_length, d_model)
        batch_size, _, seq_length, d_k = x.size()
        return x.transpose(1, 2).contiguous().view(batch_size, seq_length, self.d_model)
    
    def forward(self, Q, K, V, mask=None):
        # Build linear layers for transforming inputs and split heads
        Q = self.split_heads(self.W_q(Q))
        K = self.split_heads(self.W_k(K))
        V = self.split_heads(self.W_v(V))
        
        # Conduct scaled dot-product attention on the split heads
        attn_output = self.scaled_dot_product_attention(Q, K, V, mask)
        
        # Reassemble the multiple heads to restore the original shape and build linear layers for transforming the output
        output = self.W_o(self.combine_heads(attn_output))
        return output
    
# Define Position-Wise Feed-Forward Networks
class PositionWiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff):
        """
        The PositionWiseFeedForward class represents a neural network designed for position-wise operations. 
        It comprises two linear layers separated by a ReLU activation function. 
        In the context of transformer models, this feed-forward network is individually and uniformly applied to each position. 
        Its primary function is to modify the features acquired from the transformer's attention mechanisms, serving as an additional processing step.
        d_model: dimensionality of the model's input and output
        d_ff: dimensionality of the inner layer in the feed-forward network
        self.fc1 and self.fc2: two fully connected (linear) layers with input and output dimensions as defined by d_model and d_ff
        self.relu: ReLU (Rectified Linear Unit) activation function, which introduces non-linearity between the two linear layers by replacing all negative values with zeros
        """
        super(PositionWiseFeedForward, self).__init__()

        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))

# Define Positional Encoding
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_length):
        """
        The PositionalEncoding class incorporates positional information of tokens within a sequence. 
        Given that the transformer model lacks built-in awareness of token order, owing to its self-attention mechanism, this class aids the model in accounting for token positions within the sequence. 
        It employs sinusoidal functions selected to enable the model to effortlessly acquire the ability to attend to relative positions, yielding distinct and continuous encodings for each position in the sequence.
        d_model: the dimension of the model's input
        max_seq_length: the maximum length of the sequence for which positional encodings are pre-computed
        pe: a tensor filled with zeros, which will be populated with positional encodings
        position: a tensor containing the position indices for each position in the sequence
        div_term: a term used to scale the position indices in a specific way
        """
        super(PositionalEncoding, self).__init__()
        
        pe = torch.zeros(max_seq_length, d_model)
        position = torch.arange(0, max_seq_length, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
        
        # The sine function is applied to the even indices and the cosine function to the odd indices of pe
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        # pe is registered as a buffer, which means it will be part of the module's state but will not be considered a trainable paramete
        self.register_buffer('pe', pe.unsqueeze(0))
        
    def forward(self, x):
        # Add the positional encodings to the input x
        return x + self.pe[:, :x.size(1)]
