# https://en.wikipedia.org/wiki/Euler–Maclaurin_formula
# Integral on discrete values
m = lambda x: np.array([8,1,9,2,3])[x-1]
m(5)
m_int = lambda x_min, x_max: np.sum([m(x) for x in np.arange(x_min, x_max+1)])
m_int(1,2)
