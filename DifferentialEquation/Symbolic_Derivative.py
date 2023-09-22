from sympy import *
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True) # Ensure that all subsequent examples are formatted nicely using Unicode characters
diff(cos(x)*log(x), x)

                 cos(x)
-log(x)⋅sin(x) + ──────
                   x
