import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants

"""
electron mass	9.10938356e-31 kg
electron mass energy equivalent	8.18710565e-14 J
electron mass energy equivalent in MeV	0.5109989461 MeV
"""
"""
Planck constant over 2 pi	1.0545718e-34 J s
Planck constant over 2 pi in eV s	6.582119514e-16 eV s
"""

hbar = constants.hbar
electron_mass = constants.electron_mass
eV = constants.electron_volt

E_vals_graph = np.linspace(0, 20, 100)
E_vals_calc = np.linspace(0, 20, 100000)

# theoretical value
def calc_y1(E, w=1e-9):
    inner = ((w ** 2) * electron_mass * E) / (2 * (hbar ** 2))
    return np.tan(np.sqrt(eV * inner))

# even numbered states
def calc_y2(E, V=20):
    if E == 0:
        return 0
    return np.sqrt((V - E) / E)


# odd numbered states
def calc_y3(E, V=20):
    if V - E == 0:
        return 0
    return - np.sqrt((E) / (V - E))


def calc_y(func, E_vals):
    return list(map(lambda E: func(E), E_vals))


# Calculate energy levels
y1_calc = calc_y(calc_y1, E_vals_calc)
y2_calc = calc_y(calc_y2, E_vals_calc)
y3_calc = calc_y(calc_y3, E_vals_calc)


def find_energy_levels():
    cur_energy_level = 1
    energy_levels = []
    # loop through all E_vals, comparing the theoretical either with odd or even energy calculations
    for i in range(len(E_vals_calc)):
        if i == 0:
            continue
        if cur_energy_level % 2 != 0:
            # odd energy state, so check y3
            if np.abs(y1_calc[i] - y3_calc[i]) < .0001:
                energy_levels.append(y3_calc[i])
                cur_energy_level += 1
        else:
            # even energy state, so check y2
            if np.abs(y1_calc[i] - y2_calc[i]) < .0001:
                energy_levels.append(y2_calc[i])
                cur_energy_level += 1
        if len(energy_levels) == 6:
            return energy_levels

    return energy_levels


fig, ax = plt.subplots()

y1 = calc_y(calc_y1, E_vals_graph)
y2 = calc_y(calc_y2, E_vals_graph)
y3 = calc_y(calc_y3, E_vals_graph)

ax.plot(E_vals_graph, y1, label="y1")
ax.plot(E_vals_graph, y2, label="y2")
ax.plot(E_vals_graph, y3, label="y3")
ax.legend()
plt.show()
