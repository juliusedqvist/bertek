import math

import numpy as np
from matplotlib import pyplot as plt

from roadster import total_consumption, load_route



x = [2**i + 1 for i in range(25)]
# print(x[:-1], "n")

"""distance_km, _ = load_route("speed_anna.npz")
print(distance_km[-1])"""
y = [total_consumption(15.5, "speed_anna.npz", i) for i in x]
abs_error = [abs(y[i+1] - y[i]) for i in range(len(y[:-1]))]
# print(abs_error, "error")

p = [math.log2(abs_error[i+1]/abs_error[i]) for i in range(len(abs_error[:-1]))]
p_avg = sum(p)/len(p)
print(p, "log(error(2h)/error(h))", p_avg)
c = [abs_error[i] * x[i] ** 1.5 for i in range(len(abs_error))]
c_avg = sum(c)/len(c)
# print(c, "error*h^2", c_avg)
# Use pyplot.loglog to plot the absolute error
plt.loglog(x[:-1], abs_error, marker='o', linestyle='-', label='Absolute Error')

x2 = np.linspace(x[0], x[-1], 25)
y2 = [c_avg/(i**2) for i in x2]
plt.loglog(x2, y2)

plt.show()



