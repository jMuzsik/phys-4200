import numpy as np
import scipy.integrate as integrate

from scipy.constants import k, c, hbar, pi

"""
b)  Write a program to evaluate the integral in this expression. Explain what method 
you used, and how accurate you think your answer is.
c)  Even before Planck gave his theory of thermal radiation around the turn of the 
20th century, it was known that the total energy W given off by a black body per unit 
area per second followed Stefan’s law: W = σT4, where σ is the Stefan–Boltzmann 
constant. Use your value for the integral above to compute a value for the 
Stefan–Boltzmann constant (in SI units) to three significant figures. Check your 
result against the known value, which you can find in books or on-line. You should 
get good agreement.
"""


def integrand(x):
    return (x ** 3) / ((np.e ** x) - 1)


c = (k ** 4) / ((4 * pi ** 2) * (c ** 2) * (hbar ** 3))

# Cannot use infinity for this reason: OverflowError: (34, 'Result too large')
I, _ = integrate.quad(integrand, 0, 500)

print("Result from calculation: " + str(c * I) + "T^4.")
print("Expected value: " + "5.67 * 10 ^(-8) * T^4" + ".")
print("So, basically the same using this method.")
