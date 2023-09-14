import numpy as np
A = np.random.normal(size=(8,8))
x = np.random.normal(size=8)
b = A.dot(x)

x_hat = np.linalg.solve(A, b)

print(f'The truth of x: {x}')
print(f'The numpy solution of x: {x_hat}')
