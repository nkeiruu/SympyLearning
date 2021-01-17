#!/usr/bin/env python3
import sympy as sp
from sympy.plotting import plot3d
from sympy.plotting.plot import plot3d_parametric_line
from sympy.solvers.solveset import linsolve

#print expressions nicely
sp.init_printing()

#create symbols
x, y, z = sp.symbols('x y z')

#create expression
expr  = x**2 + 3*x -7
expr2 = sp.Eq(y, x**2)
expr3 = 4*x + 2
implicit_expr = y - x**2


#plotting 
#sp.plot(sp.sin(x), title = 'Sinusodial Function', line_color = 'yellow')
#plot implicit function(NB: defaults = 0)
#sp.plot_implicit(implicit_expr)
#plot3d(implicit_expr)
#Plot 3d surface
#plot3d(x*y, (x, -10,10), (y, -10,10))
#plot parametric line
#plot3d_parametric_line(sp.sin(x)**2, sp.cos(x), x)

#Subbing an expression(Good for evaluating)
expr = expr.subs(x,x*z)
#print(expr)

#all sympy objects immutable. Original object never changed by method except matrices.

#solve equation
ans3 = sp.solveset(expr3)
#print(ans3)

#solve linear system of equation-->linsolve
equ1 = sp.Eq(3*x + 4*y, 6)
equ2 = sp.Eq(5*x +3*y, 7)

eqlist = [equ1, equ2]
linans = linsolve(eqlist, (x,y))
print(linans)


