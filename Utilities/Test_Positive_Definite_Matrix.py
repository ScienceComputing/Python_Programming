import numpy as np
def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

A = np.array([[12, 2], [2, 1]])
is_pos_def(A)
# True
