import matplotlib.pyplot as plt
import numpy as np
import scipy as sy

nums = np.genfromtxt(fname='dow.txt')

nums_ft = np.fft.fft(nums)

nums_ft_formatted = [c.real for c in nums_ft]
print(type(nums_ft_formatted[0]))

x = range(0, len(nums))

plt.plot(x, nums)
plt.plot(x, nums_ft_formatted)
plt.show()