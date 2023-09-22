import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

x = np.linspace(-np.pi, np.pi, 500)
y = np.zeros(len(x))

orders = [0,1,2,3]

plt.figure(figsize=(4, 4))

for n in orders:
    y += (-1) ** n * x ** (2 * n + 1) / np.math.factorial(2 * n + 1) # Taylor series for sin(x) when a = 0
    plt.plot(x, y, label=f'{2 * n + 1}th Order')

plt.plot(x, np.sin(x), 'k', label = 'Analytic') # k for black
plt.grid()
plt.title('Taylor Series Approximations of Different Orders')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
