import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig = plt.figure(figsize=(5, 5))
ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
# ideally it is dynamic and infinite
# ax = plt.axes()
# ax = plt.axes(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25))
# point = plt.Circle((0, -1), 0.15, fc='b')
cur1 = (0, 0)
cur2 = (0, 10)
cur3 = (10, 0)
point1 = plt.Circle(cur1, 2, fc='b')
point2 = plt.Circle(cur2, 4, fc='g')
point3 = plt.Circle(cur3, 6, fc='r')


def init():
    ax.add_patch(point1)
    ax.add_patch(point2)
    ax.add_patch(point3)
    return point1, point2, point3,


def helper(val, movement, pos_or_neg):
    if val == 0:
        return movement * pos_or_neg
    else:
        if pos_or_neg == 1:
            return val + movement
        else:
            return val - movement


def update(tup, movement):
    direction = random.randint(0, 3)

    x = tup[0]
    y = tup[1]
    # 0: up
    # 1: right
    # 2: down
    # 3: left
    new_val = ()
    if direction == 0:
        new_val = helper(y, movement, 1)
        return (x, new_val)
    elif direction == 1:
        new_val = helper(x, movement, 1)
        return (new_val, y)
    elif direction == 2:
        new_val = helper(y, movement, -1)
        return (x, new_val)
    else:
        new_val = helper(x, movement, -1)
        return (new_val, y)


def animate(i):
    global cur1, cur2, cur3
    cur1 = update(cur1, 1)
    point1.center = cur1
    cur2 = update(cur2, 2)
    point2.center = cur2
    cur3 = update(cur3, 3)
    point3.center = cur3

    return point1, point2, point3,


anim = animation.FuncAnimation(fig, animate,
                               init_func=init, frames=1000, interval=20, blit=True)
writergif = animation.ImageMagickFileWriter()
anim.save('filename.gif', writer=writergif)
