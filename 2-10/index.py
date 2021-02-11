import sys
import math

N = float(sys.argv[1])
rule = sys.argv[2]
check_err = sys.argv[3]

def f(x):
    return x ** 4 - (2 * x) + 1

a = 0
b = 2

if rule == "trapezoid":
    h = (b - a) / N

    result = (.5 * f(a)) + (.5 * f(b))

    for i in range(N):
        result += f(a + (i * h))

    print(result * h)

elif rule == "simpson":
    h = (b - a) / N
    result = (f(a) + f(b))

    for i in range(math.floor(N / 2) + 1):
        k = (2 * i - 1)
        result += 4 * (f(a + (k * h)))

    for i in range(math.floor(N / 2)):
        k = 2 * i
        result += 2 * (f(a + (k * h)))

    print(h/3 * result)
