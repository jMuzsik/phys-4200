import numpy as np
from math import pi
import matplotlib.pyplot as plt

t = np.linspace(0, 2, num=1000)
curr = 0
# Discrete fourier transform
for k in range(0, 100):
    # Equation for fourier transform
    c = (4 / pi)
    numer = np.sin(2*pi*((2*k)-1)*t)
    denom = (2*k)-1
    curr = curr + numer/denom
    curr_sum = c * curr
    plt.plot(t, curr_sum)

plt.title("Square Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True, which="both")
plt.axhline(y=0)
plt.show()
