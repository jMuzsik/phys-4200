import math
import numpy as np
from scipy.constants import electron_mass, hbar
import matplotlib.pyplot as plt

V = 20
# 1 nm
w = 1e-9

E_vals = list(range(20))
print(E_vals)


def calc_y1(w, E):
    return math.tan(math.sqrt((w ** 2 * electron_mass * E) / (2 * hbar ** 2)))


def calc_y2(V, E):
    if E == 0:
        return 0
    return math.sqrt((V - E) / E)


def calc_y3(V, E):
    if V - E == 0:
        return 0
    return - math.sqrt((E) / (V - E))


fig, ax = plt.subplots()
ax.plot(E_vals, list(map(lambda E: calc_y1(w, E), E_vals)), label="y1")
ax.plot(E_vals, list(map(lambda E: calc_y2(V, E), E_vals)), label="y2")
ax.plot(E_vals, list(map(lambda E: calc_y3(V, E), E_vals)), label="y3")
ax.legend()
plt.show()

# not sure what the second part means...
