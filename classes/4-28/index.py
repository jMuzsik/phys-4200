import numpy as np
from scipy.optimize import minimize

import matplotlib.pyplot as plt

# parameter estimation practice from https://www.youtube.com/watch?v=AhgnJ75FTMU


def specific_heat(p, theta):
    # extract individual parameters from p vector
    A = p[0]
    alpha = p[1]
    B = p[2]
    D = p[3]

    # return specific heat
    return (A/alpha) * np.power(theta, -alpha) * (1.0 + D * np.power(theta, 0.5)) + B


def objective(q, theta_warm, theta_cold, c_warm_exp, c_cold_exp):
    # extract the parameters from the array q and calculate the specific heat
    # on the warm side
    # (A, APrime, alpha, B, D, Dprime)
    p = [q[0], q[2], q[3], q[4]]
    c_warm = specific_heat(p, theta_warm)

    # extract the parameters from the array q and calculate the specific heat
    # on the warm side
    p = [q[1], q[2], q[3], q[5]]
    c_cold = specific_heat(p, theta_cold)

    error_warm_sq = np.square(c_warm - c_warm_exp)
    error_cold_sq = np.square(c_cold - c_cold_exp)

    return np.sum(error_warm_sq) + np.sum(error_warm_sq)


#  Import raw data
raw_cold_data = np.loadtxt('cold_data.txt')
raw_warm_data = np.loadtxt('warm_data.txt')

#  The temperature and specific heat are in the first and seconds columns,
#  respectively.  We pull them into their own variables for simplicity's
#  sake
theta_warm = raw_warm_data[0, :]
c_warm = raw_warm_data[1, :]

theta_cold = raw_cold_data[0, :]
c_cold = raw_cold_data[1, :]

# initial guesses
# Format is (A, APrime, alpha, B, D, Dprime)
q = [7.0, 10.0, -0.021, 375.0, -0.01, -0.01]

results = minimize(objective, q, args=(
    theta_warm, theta_cold, c_warm, c_cold), method='Powell')

print(results)
# plt.plot(theta_warm, c_warm, 'or')
# plt.plot(theta_cold, c_cold, 'ob')
# plt.show()
