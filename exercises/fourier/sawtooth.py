import numpy as np
from math import pi
import matplotlib.pyplot as plt

t = np.linspace(0, 3, num=1000)
curr = 0
for k in range(1, 100):
    const = 2 / pi
    numer = ((-1)**k) * np.sin(2*pi*t*k)
    denom = k
    curr = curr + numer/denom
    curr_sum = const * curr
    plt.plot(t, curr_sum)

plt.title("Sawtooth Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True, which="both")
plt.axhline(y=0, color="k")
plt.show()
