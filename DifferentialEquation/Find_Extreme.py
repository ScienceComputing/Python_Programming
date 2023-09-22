import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Use the derivative to find the maximum of a function
F = lambda x: -x**2 + 5*x - 2
F_prime = lambda x: -2*x + 5

# Plot the function and its tangent line at x=5/2
x = 5/2
x_grid = np.linspace(-6,6,100)
plt.plot(x_grid, F(x_grid), label='$F(x)$', color='blue', zorder=1)
plt.scatter(x, F(x), color='black', zorder=2)
plt.plot(x_grid, y_1(x, x_grid), color='red', zorder=3, label='Tangent line')
plt.legend(loc='upper left')
plt.xlabel('x')


# Use the derivative to find the minimum of a function
F = lambda x: x**2 + 5*x - 2
F_prime = lambda x: 2*x + 5

# Plot the function and its tangent line at x=-5/2
x = -5/2
x_grid = np.linspace(-6,6,100)
plt.plot(x_grid, F(x_grid), label='$F(x)$', color='blue', zorder=1)
plt.scatter(x, F(x), color='black', zorder=2)
plt.plot(x_grid, y_1(x, x_grid), color='red', zorder=3, label='Tangent line')
plt.legend(loc='upper left')
plt.xlabel('x')
