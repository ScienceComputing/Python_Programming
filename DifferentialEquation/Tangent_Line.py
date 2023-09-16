import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Use the point slope formula to obtain the tangent curve at x. 
# y1 - y0 = slope * (x1 - x0)
y_1 = lambda x_0, x_1: F_prime(x_0) * (x_1 - x_0) + F(x_0)

# Plot the function and its tangent line at x = 5
x_0 = 5
x_1 = np.linspace(0,6,100)
plt.plot(x_1, F(x_1), label='$F(x)$', color='blue', zorder=1)
plt.scatter(x_0, F(x_0), color='black', zorder=2)
plt.plot(x_1, y_1(x_0, x_1), color='red', zorder=3, label='Tangent line')
plt.legend(loc='upper left')
plt.xlabel('x')
