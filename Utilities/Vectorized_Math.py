import time
from collections import deque
import numpy as np

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
