import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

# params = {"R": .08, "m": 1, "angle": 0.523599, "v": 100, "p": 1.22, "C": .47}
def AirResistanceFunc(x, params):
    R = params["R"]
    m = params["m"]
    angle = params["angle"]
    v = params["v"]
    p = params["p"]
    C = params["C"]

    return 0.5 * constants.pi * (R ** 2) * p * C * (v ** 2)


def RungeKutta4(f, x0, t0, tf, dt):

    t = np.arange(t0, tf, dt)
    nt = t.size

    nx = x0.size
    x = np.zeros((nx, nt))

    x[:, 0] = x0

    for k in range(nt - 1):
        k1 = dt*f(t[k], x[:, k])
        k2 = dt*f(t[k] + dt/2, x[:, k] + k1/2)
        k3 = dt*f(t[k] + dt/2, x[:, k] + k2/2)
        k4 = dt*f(t[k] + dt, x[:, k] + k3)

        dx = (k1 + 2 * k2 + 2 * k3 + k4) / 6

        x[:, k+1] = x[:, k] + dx

    return x, t

# R is radius, m is mass, angle in radians, v is initial velocity, p is density of air, C is coefficient of drag
params = {"R": .08, "m": 1, "angle": 0.523599, "v": 100, "p": 1.22, "C": .47}


def f(t, x): return AirResistanceFunc(x, params)


x0 = np.array([0,0])

# solve the diff eq.

t0 = 0
tf = 100
dt = .01

x, t = RungeKutta4(f, x0, t0, tf, dt)

# plt.plot(t, x[0])
# plt.show()

# plt.subplot(1, 2, 1)
# plt.plot(t, x[0, :], "r", label="Preys")
# plt.plot(t, x[1, :], "b", label="Predators")
# plt.xlabel("Time (t)")
# plt.grid()
# plt.legend()

# plt.subplot(1, 2, 2)
# plt.plot(x[0, :], x[1, :])
# plt.xlabel("Preys")
# plt.ylabel("Predators")
# plt.grid()
# plt.tight_layout()
# plt.show()