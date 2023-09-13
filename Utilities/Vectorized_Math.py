import time
from collections import deque
import numpy as np

"""
Case 1
"""
# The fatest vectorized solution
t0 = time.time()
data = np.array([9, 2, 7, 8, 10, 2, 7])
squared_data = data**2
t1 = time.time()
print(t1 - t0)


t0 = time.time()
data = [9, 2, 7, 8, 10, 2, 7]
squared_data = deque()
for item in data:
    squared_data.append(item**2)

t1 = time.time()
print(t1 - t0)


t0 = time.time()
data = [9, 2, 7, 8, 10, 2, 7]
squared_data = []
for item in data:
    squared_data.append(item**2)

t1 = time.time()
print(t1 - t0)


t0 = time.time()
data = [9, 2, 7, 8, 10, 2, 7]
squared_data = []
squared_data = [item**2 for item in data]

t1 = time.time()
print(t1 - t0)


"""
Case 2
"""
import numpy as np
m = np.array([0,3,-9])
n = np.array([0.2,8,7])

# Do the inner product using for loop (not recommended due to its slow processing speed)
inner_product_for_loop = 0
for i in range(3):
  inner_product_for_loop += m[i] * n[i]

print(inner_product_for_loop)

# Do the inner product using numpy
inner_product_numpy = m.dot(n)

assert inner_product_for_loop == inner_product_numpy

# Interpret: numpy executes the code in precompiled C operation, which speeds up the running time for the code.
# It is recommended to vectorize the code whenever possible.
