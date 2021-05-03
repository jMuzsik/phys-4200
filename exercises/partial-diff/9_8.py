from __future__ import division, print_function
from pylab import *
from banded import banded
from os import sys
from vpython import curve, rate
sys.path.append('cpresources')

h = 1e-18*10
hbar = 1.0546e-36
L = 1e-8
M = 9.109e-31
N = 1000  # Grid slices

a = L/N

a1 = 1 + h*hbar/2/M/a**2*1j
a2 = -h*hbar*1j/4/M/a**2
b1 = 1 - h*hbar/2/M/a**2*1j
b2 = h*hbar*1j/4/M/a**2

ksi = zeros(N+1, complex)


def ksi0(x):
    x0 = L/2
    sigma = 1e-10
    k = 5e10
    return exp(-(x-x0)**2/2/sigma**2)*exp(1j*k*x)


x = linspace(0, L, N+1)
ksi[:] = ksi0(x)
ksi[[0, N]] = 0


A = empty((3, N), complex)

A[0, :] = a2
A[1, :] = a1
A[2:, ] = a2


arr = []

# setup vectors with solely x values
for i in range(len(x)):
    arr.append([x[i] - L/2, 0, 0])

ksi_c = curve(pos=arr)

n = len(arr)


def update_points(ksi_c, y, z):
    for i in range(n):
        ksi_c.modify(i, y=y[i], z=z[i])


while True:
    rate(30)
    y = real(ksi)*1e-9
    z = imag(ksi)*1e-9
    # update at each point, keeping x
    update_points(ksi_c, y, z)
    for i in range(20):
        v = b1*ksi[1:N] + b2*(ksi[2:N+1] + ksi[0:N-1])
        ksi[1:N] = banded(A, v, 1, 1)
