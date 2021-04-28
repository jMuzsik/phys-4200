import numpy as np
import scipy.integrate as integrate

from scipy.constants import k, c, hbar, pi

def integrand(x):
    return (x ** 3) / ((np.e ** x) - 1)


c = (k ** 4) / ((4 * pi ** 2) * (c ** 2) * (hbar ** 3))

# Cannot use infinity for this reason: OverflowError: (34, 'Result too large')
I, _ = integrate.quad(integrand, 0, 500)

print("Result from calculation: " + str(c * I) + "T^4.")
print("Expected value: " + "5.67 * 10 ^(-8) * T^4" + ".")
print("So, basically the same using this method.")
