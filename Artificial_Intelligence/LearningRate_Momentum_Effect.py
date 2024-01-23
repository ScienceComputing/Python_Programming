import torch
import numpy as np
import matplotlib.pyplot as plt

def my_function(input_value):
    """Calculate a custom function of the input."""
    return input_value**4 + 2*input_value**3 - 7*input_value**2 + 9

def plot_parameter_impact(learning_rate=0.01, momentum_factor=0.0):
    """Optimize a custom function using gradient descent with optional momentum and plot the results."""

    initial_x = torch.tensor(2.0, requires_grad=True)
    buffer = torch.zeros_like(initial_x.data)
    optimization_values = []

    for i in range(20):
        y = my_function(initial_x)
        optimization_values.append((initial_x.clone(), y.clone()))
        y.backward()

        gradient = initial_x.grad.data
        if momentum_factor != 0:
            buffer.mul_(momentum_factor).add_(gradient)
            gradient = buffer

        initial_x.data.add_(gradient, alpha=-learning_rate)
        initial_x.grad.zero_()

    x_values = np.arange(-3, 2, 0.001)
    y_values = my_function(x_values)

    plt.figure(figsize=(10, 5))
    plt.plot([v[0].detach().numpy() for v in optimization_values], [v[1].detach().numpy() for v in optimization_values], 'r-X',
             linewidth=2, markersize=7)

    for i in range(20):
        plt.text(optimization_values[i][0] + 0.1, optimization_values[i][1], f'step {i}', fontdict={'color': 'r'})

    plt.plot(x_values, y_values, linewidth=2)
    plt.grid()
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.legend(['Optimizer steps', 'My function'])
    plt.show()

plot_parameter_impact(learning_rate=0.001)
plot_parameter_impact(learning_rate=0.072)
plot_parameter_impact(momentum_factor=0.05)
plot_parameter_impact(momentum_factor=0.935)
