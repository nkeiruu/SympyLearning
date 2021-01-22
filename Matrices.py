import sympy as sp

a, b = sp.symbols('a b')

#create matrix manually. A list of lists. for column vector exclude external list.
M = sp.Matrix([[1,3],[98,6]])

#create identity matrix
I = sp.eye(4)

#create zero matrix
zeroM = sp.zeros(2,2)

#multiply a matrice by scalar
M_by_2 = 2*M

#invert Matrix
M_inverted = M**-1

#Matrix multiplication
MM = M_by_2*zeroM

#Symbols in matrices
MS = sp.Matrix([a,b])
MN = sp.Matrix([[2,2]])
M_symbol = MS*MN

print(M , I, M_by_2 , M_inverted, MM, M_symbol)