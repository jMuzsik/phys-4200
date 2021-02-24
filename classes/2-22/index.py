import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return 1 + (.5) * np.tanh(2 * x)

def calc_der(x, delta):
    return (f(x + delta) - f(x)) / delta

steps = 10
deltas = np.linspace(-2, 2, num=steps)

h = 4 / steps

results = []

for delta in deltas:
  results.append(calc_der(delta, h))

print(results)

plt.plot(results, deltas)
plt.xlabel("calculated derivatives")
plt.ylabel("δ")
plt.title("Derivatives vs δ")
plt.show()