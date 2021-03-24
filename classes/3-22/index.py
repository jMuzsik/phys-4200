
import numpy as np
import math
import random
from matplotlib import pyplot as plt

PI = 3.1415926
e = 2.71828


def get_rand_number(min_value, max_value):
    range = max_value - min_value
    choice = random.uniform(0, 1)
    return min_value + range*choice

# lets also define the function we want to integrate over f(x)


def f_of_x(x):
    return np.sin(1 / (x * (2-x))) ** 2


def crude_monte_carlo(num_samples=5000):
    lower_bound = 0
    upper_bound = 2

    sum_of_samples = 0
    for i in range(num_samples):
        x = get_rand_number(lower_bound, upper_bound)
        sum_of_samples += f_of_x(x)

    return (upper_bound - lower_bound) * float(sum_of_samples/num_samples)


def get_crude_MC_variance(num_samples):
    int_max = 5 # this is the max of our integration range
    
    # get the average of squares
    running_total = 0
    for i in range(num_samples):
        x = get_rand_number(0, int_max)
        running_total += f_of_x(x)**2
    sum_of_sqs = running_total*int_max / num_samples
    
    # get square of average
    running_total = 0
    for i in range(num_samples):
        x = get_rand_number(0, int_max)
        running_total = f_of_x(x)
    sq_ave = (int_max*running_total/num_samples)**2
    
    return sum_of_sqs - sq_ave


MC_samples = 10000
var_samples = 10000 # number of samples we will use to calculate the variance
crude_estimation = crude_monte_carlo(MC_samples)
variance = get_crude_MC_variance(var_samples)
error = math.sqrt(variance/MC_samples)

# display results
print("Monte Carlo Approximation of f(x):", crude_estimation)
print("Variance of Approximation:", variance)
print("Error in Approximation:", error)