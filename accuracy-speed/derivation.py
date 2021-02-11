import matplotlib.pyplot as plt

"""
a)  Write a program that defines a function f(x) returning the value x(x−1), then 
calculates the derivative of the function at the point x = 1 using the formula above
with δ = 10−2. Calculate the true value of the same derivative analytically and 
compare with the answer your program gives. The two will not agree perfectly. 
Why not?
b)  Repeat the calculation for δ = 10−4, 10−6, 10−8, 10−10, 10−12, and 10−14. You 
should see that the accuracy of the calculation initially gets better as δ gets 
smaller, but then gets worse again. Plot your result as a function of δ. 
Why is this?
"""

# shared code


def print_info(calc, error):
    print("Result from calculation: " + str(calc) + ".")
    print("Off by: " + str(error) + ".")


def f(x):
    return x * (x - 1)


def calc_der(x, delta):
    return (f(x + delta) - f(x)) / delta


deltas = [10 ** -2, 10 ** -4, 10 ** -6,
          10 ** -8, 10 ** -10, 10 ** -12, 10 ** -14]
x = 1
true_value = 1
results = []

# Part a

print("Part A/B:")

for delta in deltas:
    calc = calc_der(x, delta)
    error = abs(true_value - calc)
    print_info(calc, error)
    results.append(calc)

plt.plot(results, deltas)
plt.xlabel("calculated derivatives")
plt.ylabel("δ")
plt.title("Derivatives vs δ")
plt.show()
