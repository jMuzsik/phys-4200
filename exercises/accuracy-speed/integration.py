import numpy as np
import math

"""
a)  Write a program to evaluate the integral above with N = 100 and compare 
    the result with the exact value. The two will not agree very well, because 
    N = 100 is not a sufficiently large number of slices.
b)  Increase the value of N to get a more accurate value for the integral. If 
    we require that the program runs in about one second or less, how accurate 
    a value can you get?
"""

def print_info(calc, error):
    print("Result from calculation: " + str(calc) + ".")
    print("Off by: " + str(error) + ".")


def f(x):
    return math.sqrt(1 - x ** 2)

curr = -1
N = 100
true_value = np.pi / 2
result = 0.0
step = 2 / N

# Part a

print("Part A/B:")

for i in range(N):
    result += step * f(curr)
    curr += step

print("Result for when N = 100:")
error = abs(true_value - result)
print_info(result, error)

N = 10000
result = 0.0
curr = -1
step = 2 / N
for i in range(N):
    result += step * f(curr)
    curr += step

print("Result for when N = 10000:")
error = abs(true_value - result)
print_info(result, error)

print("Within a second we can get very close to the true value.")