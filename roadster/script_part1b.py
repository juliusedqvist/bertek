import roadster
import numpy as np
import matplotlib.pyplot as plt
import math

elsa_distance_km, elsa_speed_kmph = roadster.load_route('speed_elsa.npz')
anna_distance_km, anna_speed_kmph = roadster.load_route('speed_anna.npz')

# anna1 = roadster.plot_route('speed_anna.npz')
# elsa1 = roadster.plot_route('speed_elsa.npz')

x_anna = anna_distance_km  # np.linspace(0, anna_distance_km[-1], len(anna_distance_km)) # Samma antal punkter
x_elsa = elsa_distance_km  # np.linspace(0, elsa_distance_km[-1], len(elsa_distance_km))

anna2 = roadster.velocity(x_anna, 'speed_anna.npz')
plt.plot(x_anna, anna2, label='Anna')
# scatter plot of anna distance speed
plt.scatter(anna_distance_km, anna_speed_kmph, s=1)
plt.show()
