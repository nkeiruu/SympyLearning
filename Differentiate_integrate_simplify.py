import sympy as sp
x, y, z = sp.symbols('x y z')
expr = 6*x +7*x**2 + y
trig_expr = sp.sin(x)**2 + sp.cos(x)**2
expr7 = x*(y+x+z)

#Differentiate wrt x
expr2 = expr.diff(x)

#Differentiate wrt y
expr3 = expr.diff(y)

#intergrate wrt y
expr4 = expr.integrate(x)

#Simplify
expr5 = sp.simplify(trig_expr)

#Expand
expr6 = sp.expand(expr7)

#Factor
expr8 = sp.factor(expr6)

print(f"Differentiated wrt x: {expr2}\n"
      f"Differentiated wrt y: {expr3}\n"
      f"Integrated wrt y: {expr4}\n"
      f"The expression {trig_expr} is simplfied to {expr5}\n"
      f"The expression {expr7} is simplfied to {expr6}\n")
         
