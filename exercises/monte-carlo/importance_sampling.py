import numpy as np
import math
import random
from matplotlib import pyplot as plt
from IPython.display import clear_output

PI = 3.1415926
e = 2.71828

# predominantly followed this example:
# https://towardsdatascience.com/monte-carlo-simulations-with-python-part-1-f5627b7d60b0
def get_rand_number(min_value, max_value):
    range = max_value - min_value
    choice = random.uniform(0, 1)
    return min_value + range*choice


def f_of_x(x):
    if x == 0:
        return 0
    return ((x ** (-0.5)) / ((e ** x) + 1))


def p_of_x(x):
    return 1 / (2 * math.sqrt(x))


xs = np.linspace(0, 1, 10000)
ys = [f_of_x(x) for x in xs]
plt.plot(xs, ys)
plt.title("f(x)")
plt.show()
