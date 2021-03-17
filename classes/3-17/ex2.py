import numpy as np
from random import random
import matplotlib.pyplot as plt

thallium_num = 100
lead_num = 0

half_life = 3.053 * 60
mu = 1.0 / half_life


def f(x):
    return (-1.0 / mu) * np.log10(1.0 - x)


x = np.arange(0.0, thallium_num, 1.0)

thallium_over_time = []
lead_over_time = []

for i in range(len(x)):
    print(f(float(i)))

# plt.plot(x, thallium_over_time, label="Thallium")
# plt.plot(x, lead_over_time, label="Lead")
# plt.xlabel("Time")
# plt.ylabel("Number of atoms")
# plt.legend()
# plt.show()
