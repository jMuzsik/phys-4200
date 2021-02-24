import math

import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
    description='''
    Problems related to lab one - Programming for Physicist.
    There are two problems, requiring the use of --prob.
        (a) Requires height (--height) and time (--time). 
        (b) Requires relativistic speed (--speed) and lightyears (--lightyears).
    ''', formatter_class=RawTextHelpFormatter)
parser.add_argument('--prob', help="height or relativistic")
parser.add_argument('--height', help="height of tower")
parser.add_argument('--time', help="time object is falling")
parser.add_argument(
    '--speed', help="relativistic speed as fraction of speed of light")
parser.add_argument('--lightyears', help="light years away")

args = parser.parse_args()

prob, height, time, speed, lightyears = [
    args.prob, args.height, args.time, args.speed, args.lightyears]

# Funcs related to falling object

def height_func(h, t):
    g = 9.81
    res = h - (.5 * g * t ** 2)
    if res < 0:
        return 0
    return res


def check_height_args(h, t):
    if t < 0:
        return "Time must be greater than 0 to calculate height."
    if h <= 0:
        return "Height must be greater than 0 to calculate height."
    return False

# Funcs related to relativistic calc

def relativistic_func(v, x):
    print(x, v, 1 - v ** 2)
    return [x / v, x * math.sqrt(1 - (v ** 2))]


def check_relativistic_args(v, lightyears):
    if v < 0:
        return "The speed must be greater than 0."
    elif v > 1:
        return "The speed cannot be greater than the speed of light, it must be a fraction."
    if lightyears <= 0:
        return "Must be more than 0 lightyears away."
    return False


if prob == 'height':
    """
    A ball is dropped from a tower of height h with initial velocity zero. 
    Write a program that asks the user to enter the height in meters of the 
    tower and then calculates and prints the time the ball takes until it 
    hits the ground, ignoring air resistance. Use your program to calculate 
    the time for a ball dropped from a 100 m high tower.
    """
    height = float(height)
    time = float(time)
    err = check_height_args(height, time)
    if type(err) is str:
        print(err)
    else:
        res = height_func(height, time)
        print("The current height of the ball is: " + str(res) + ".")
elif prob == 'relativistic':
    """
    A spaceship travels from Earth in a straight line at relativistic speed v to 
    another planet x light years away. Write a program to ask the user for the 
    value of x and the speed v as a fraction of the speed of light c, then print 
    out the time in years that the spaceship takes to reach its destination (a) 
    in the rest frame of an observer on Earth and (b) as perceived by a passenger 
    on board the ship. Use your program to calculate the answers for a planet 10 
    light years away with v = 0.99c.
    """
    speed = float(speed)
    lightyears = float(lightyears)
    err = check_relativistic_args(speed, lightyears)
    if type(err) is str:
        print(err)
    else:
        rest_frame, relativistic_frame = relativistic_func(speed, lightyears)
        print("The rest frame time is: " + str(rest_frame) + "years.")
        print("The relativistic frame time is: " +
              str(relativistic_frame) + "years.")
else:
    parser.print_help()
