# https://en.wikipedia.org/wiki/Euler–Maclaurin_formula

# Case 1: integral on discrete values is equivalent to the summation of f(x) over discrete instances of x
m = lambda x: np.array([8,1,9,2,3])[x-1]
m(5)
m_int = lambda x_min, x_max: np.sum([m(x) for x in np.arange(x_min, x_max+1)])
m_int(1,2)

# Case 2: culumative distribution function on a discrete random variable
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n, p = 10, 0.5 # We have 10 events and set the probability of getting a successful event as 0.5
x = np.arange(0, n+1) # Return evenly spaced values within a given interval; x is a discrete random variable
prob = binom.cdf(x, n, p)
# array([9.76562500e-04, 1.07421875e-02, 5.46875000e-02, 1.71875000e-01, 3.76953125e-01, 6.23046875e-01, 8.28125000e-01, 9.45312500e-01, 9.89257812e-01, 9.99023438e-01, 1.00000000e+00])

fig, ax = plt.subplots(1, 1)
ax.step(x, binom.cdf(x, n, p), label='binom cdf') # Show the cumulative distribution function of the binomial distribution in a step plot
