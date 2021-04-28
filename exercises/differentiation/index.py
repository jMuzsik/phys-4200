import math
import numpy as np
from scipy.constants import pi, epsilon_0
import matplotlib.pyplot as plt

def calc_radius(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def calc_potential(q, r):
    bottom = (4 * pi * epsilon_0 * r)
    if bottom != 0:
        return (q / (4 * pi * epsilon_0 * r))
    return 0

def create_grid():
    [q1, q2] = 1, -1
    [m, cm] = 1, .01
    size = int(m / cm)
    # array of correct dimensions 100 rows, 100 columns
    matrix = np.zeros((size, size))
    # each charge is 10 cm from the other, each cm is a single column
    mid = len(matrix) // 2
    # charge coordinates
    q1_x = mid - 5
    q2_x = mid + 5
    q_y = 50
    # go through matrix, input values
    for i in range(size):
        for j in range(size):
            # calc potentials at point
            p1 = calc_potential(q1, calc_radius(i, j, q1_x, q_y))
            p2 = calc_potential(q2, calc_radius(i, j, q2_x, q_y))
            p = p1 + p2
            matrix[i][j] = p
    return matrix


grid = create_grid()

# potentials
# plt.matshow(grid)
# plt.colorbar()
# plt.show()

# # electric field
# grad_x, grad_y = np.gradient(grid)
# E = np.sqrt(grad_x ** 2 + grad_y ** 2)
# plt.quiver(-grad_y[::4, ::4], grad_x[::4, ::4])
# plt.show()
