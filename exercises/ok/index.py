import numpy as np
from cmath import exp, pi
import matplotlib.pyplot as plt

"""
Write Python programs to calculate the coefficients in the discrete Fourier transforms 
of the following periodic functions sampled at N = 1000 evenly spaced points, and make 
plots of their amplitudes:

a) A single cycle of a square-wave with amplitude 1
b) The sawtooth wave yn = n
c) The modulated sine wave yn = sin(πn/N) sin(20πn/N)
"""

y1 = (np.sin((2.0 * pi) * ((2.0 * i) - 1))) / ((2.0 * i) - 1)

N = 1000

c = np.zero(N, complex)
n = np.arange(N)
for i in range(N):
    c[i] = np.sum(y * np.exp(-2j * np.pi * i * n / N))

plt.figure(figsize=(12, 4))
plt.plot(np.imag(c), label="imag")
plt.plot(np.real(c), label="real")
plt.legend()

plt.show()
