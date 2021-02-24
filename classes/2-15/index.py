from Gaussxw import gaussxwab

N = 300
a = 0
b = 2


def f(x):
    return x ** 4 - 2 * x + 1


x, w = gaussxwab(N, a, b)

sum = 0

for i in range(N):
    sum += f(x[i]) * w[i]

print("result: ", sum)
