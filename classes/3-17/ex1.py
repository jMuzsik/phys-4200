import numpy as np
from random import random 
import matplotlib.pyplot as plt

thallium_num = 100
lead_num = 0

half_life = 3.053 * 60
p = 1 - 2 ** (-1.0/half_life)

x = np.arange(0.0, thallium_num, 1.0)

thallium_over_time = []
lead_over_time = []

for i in range(len(x)):
  thallium_over_time.append(thallium_num)
  lead_over_time.append(lead_num)

  # Check each individual thallium atom
  for i in range(thallium_num):
    # check if decay
    if random() < p:
      thallium_num -= 1
      lead_num += 1

plt.plot(x, thallium_over_time, label="Thallium")
plt.plot(x, lead_over_time, label="Lead")
plt.xlabel("Time")
plt.ylabel("Number of atoms")
plt.legend()
plt.show()