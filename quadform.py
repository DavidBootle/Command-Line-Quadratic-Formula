# COPYRIGHT DAVID BOOTLE 2021

# Takes three arguments, a, b, and c, and find the solution using the quadratic formula.

import cmath
from fractions import Fraction

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

# calculate the discriminant (the area inside the square root)
d = (b**2) - (4*a*c)

# find the two solutions
sol1 = ( -b - cmath.sqrt(d) ) / (2 * a)
sol2 = ( -b + cmath.sqrt(d) ) / (2 * a)

# parse solutions
def parseSol(sol):

    # if there is an imaginary, then return as an imaginary number
    if sol.imag != 0.0:
        return sol
    
    sol = sol.real # sol is now a float value

    # if sol is an integer, return the integer value
    if sol.is_integer():
        return int(sol)
    
    # determine if the solution is a fraction
    frac = Fraction(sol).limit_denominator()

    if len(str(frac.numerator)) > 5 or len(str(frac.denominator)) > 5:
        return sol # return as a float
    else:
        return frac # return as a fraction

sol1 = parseSol(sol1)
sol2 = parseSol(sol2)

print('The solutions are {0} and {1}'.format(sol1, sol2))