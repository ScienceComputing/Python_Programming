from sympy import *
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True) # Ensure that all subsequent examples are formatted nicely using Unicode characters
diff(cos(x)*log(x), x)

                 cos(x)
-log(x)⋅sin(x) + ──────
                   x

# Solve an ode equation dx/dt + x = 6
from sympy import dsolve, Eq, symbols, Function
t = symbols('t')
x = symbols('x', cls=Function)
ode_eq = Eq(x(t).diff(t), 6 - x(t)) # Eq(Derivative(x(t), t), 6 - x(t))
ode_sol = dsolve(ode_eq, x(t))
ode_sol
# Eq(x(t), C1*exp(-t) + 6)
