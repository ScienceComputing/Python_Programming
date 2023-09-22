# Represent the mathematical objects approximately
import math
math.sqrt(18)
# 4.242640687119285

# Represent the mathematical objects symbolically
import sympy
sympy.sqrt(18)
# 3*sqrt(2)

# Compute the symbolic expressions with variables
from sympy import symbols
x, y = symbols('x y')
expr = 5*x - 6*y
expr
# 5*x - 6*y

expr + 6*y
# 5*x

expr + 10
# 5*x - 6*y + 10

y*(expr)
# y*(5*x - 6*y)

# Show the expanded or factored form of an expression
from sympy import expand, factor
expand_expr = expand(y*(expr))
expand_expr
# 5*x*y - 6*y**2

factor_expr = factor(expand_expr)
factor_expr
# y*(5*x - 6*y)
