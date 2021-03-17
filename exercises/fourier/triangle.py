import numpy as np
from math import pi
import matplotlib.pyplot as plt

t = np.linspace(0, 2, num=1000)

curr = 0
for n in range(0, 10):
    const = (2 / pi)
    numer = ((-1)**n) * np.sin(2*pi*(2*n+1)*t)
    denom = (2*n+1)**2
    curr = curr + numer/denom
    curr_sum = const * curr
    plt.plot(t, curr_sum)

plt.title("Triangle Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True, which="both")
plt.axhline(y=0, color="k")
plt.show()
