import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import linalg

# practice of crank nic from youtube video
# youtube.com/watch?v=oXx6q6cxORk
# Utilising wave equation and FTCS method

# VERSION ONE
c = 100

x = np.linspace(0, 1, 101)
a = 1/100

time = np.linspace(0, .01, 1001)
h = 0.01/1000

y = np.zeros(101)
# strike string so it vibrates at a specific freq
v = x*(1-x)*np.exp(-(x-0.5)**2/100)

shape = []
for t in time:
    shape.append(y.copy())
    v_copy = v.copy()
    denom = a**2*(y[2:] + y[:-2] - 2*y[1:-1])
    if denom.any() != 0:
      v[1:-1] += h*c**2/a**2*(y[2:] + y[:-2] - 2*y[1:-1])
    y[1:-1] += h*v_copy[1:-1]  # use v before it's changed

skip = 10

# fig = plt.figure()
# line, = plt.plot([])
# plt.xlim(0, 1)
# plt.ylim(-1e-3, 1e-3)

# def animate(frame):
#     y = shape[frame*skip]
#     line.set_data(x, y)


# anim = animation.FuncAnimation(fig, animate, frames=len(shape)//skip, interval=20)
# writergif = animation.FuncAnimation.ImageMagickFileWriter()
# anim.save('filename.gif', writer=writergif)

# VERSION 2
x = np.linspace(0, 1, 101)
a = 1/100

time = np.linspace(0, .01, 10**5+1)
h = 1/1e5

y = np.zeros(101)
# strike string so it vibrates at a specific freq
v = x*(1-x)*np.exp(-(x-0.5)**2/100)

k = .25*h**2*c**2/a**2
A1 = 1 + 2*k
A2 = -k
A = np.zeros((3, 99)) # exclude BCs 99 = 101 - 2
A[0] = A2
A[1] = A1
A[2] = A2

shape = []
for t in time:
  shape.append(y.copy())
  y_old = y.copy()
  b = k*y[:-2] + (1 -2*k)*y[1:-1] + k*y[2:] +h*v[1:-1]
  y[1:-1] = linalg.solve_banded((1,1), A, b)
  v[1:-1] += 2*k/h * (y[:-2] +y[2:] -2*y[1:-1] + y_old[:-2] +y_old[2:] -2*y_old[1:-1])

shape = np.array(shape)
plt.plot(time, shape[:, 51])
plt.show()