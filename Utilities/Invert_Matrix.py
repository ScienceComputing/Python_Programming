# Create a random square 3x3 matrix
Z_2 = np.random.random(size=(3,3))

# Invert this matrix
Z_2_inv = np.linalg.inv(Z_2)

# Inverting a matrix scales cubicly in the matrix rank
import time
inv_times = np.zeros(10)
for i,k in enumerate(range(100, 1001, 100)):
  Z = np.random.normal(size=(k,k))
  # Time how long it takes to invert a matrix with the growing size
  start_time = time.time()
  Z_inv = np.linalg.inv(Z)
  end_time = time.time()
  inv_times[i] = end_time - start_time

# Visulize the time required to invert a matrix as the matrix size grows
plt.plot(np.arange(100, 1001, 100), inv_times / inv_times[0])
plt.xlabel('Size of the original matrix')
plt.ylabel('Relative time to invert (vs time used to inverst the first matrix)')
plt.title('10x size increase = 200x computation!')
