import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Show the chain rule of derivatives
m = lambda x: x ** 3 + 6
n = lambda x: 3 * x - 1
F = lambda x: m(n(x))

m_prime = lambda x: 3 * (x ** 2)
n_prime = lambda x: 3
F_prime = lambda x: m_prime(n(x)) * n_prime(x)
y_1 = lambda x_0, x_1: F_prime(x_0) * (x_1 - x_0) + F(x_0)

# Plot the function and its tangent line at x=2
x = 2
x_grid = np.linspace(0,5,100)
plt.plot(x_grid, F(x_grid), label='$F(x)$', color='blue', zorder=1)
plt.scatter(x, F(x), color='black', zorder=2)
plt.plot(x_grid, y_1(x, x_grid), color='red', zorder=3, label='Tangent line')
plt.legend(loc='upper left')
plt.xlabel('x')
