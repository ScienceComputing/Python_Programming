# Neural Ordinary Differential Equations [NeurIPS18]: https://arxiv.org/pdf/1806.07366.pdf
# https://www.youtube.com/watch?v=V6nGT0Gakyg
"""
We introduce a new family of deep neural network models. 
Instead of specifying a discrete sequence of hidden layers, we parameterize the derivative of the hidden state using a neural network. 
The output of the network is computed using a black- box differential equation solver. 
These continuous-depth models have constant memory cost, adapt their evaluation strategy to each input, and can explicitly trade numerical precision for speed. 
We demonstrate these properties in continuous-depth residual networks and continuous-time latent variable models. 
We also construct continuous normalizing flows, a generative model that can train by maximum likelihood, without partitioning or ordering the data dimensions. 
For training, we show how to scalably backpropagate through any ODE solver, without access to its internal operations. 
This allows end-to-end training of ODEs within larger models.
"""
