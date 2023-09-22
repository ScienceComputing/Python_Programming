from sympy import *
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True) # Ensure that all subsequent examples are formatted nicely using Unicode characters
integrate(sin(x) + 6, x)
# 6*x - cos(x)

integrate(sin(x) + 6, (x, -1, 1)) # Compute the definite integrals
# 12
