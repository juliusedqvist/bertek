import roadster
import matplotlib.pyplot as plt

#loads and stores Annas and Elsas route distance and speed
anna_distance_km, anna_speed_kmph = roadster.load_route('speed_anna')
elsa_distance_km, elsa_speed_kmph = roadster.load_route('speed_elsa')

#x_anna =np.linspace(0.,anna_distance_km[-1],num=40000) #alternative
#x_elsa =np.linspace(0.,elsa_distance_km[-1],num=20000) #alternative

x_anna = anna_distance_km
x_elsa = elsa_distance_km

#calls the velocity function in the roadster module for interpolation
anna_velocity = roadster.velocity(x_anna, 'speed_anna')
elsa_velocity = roadster.velocity(x_elsa, 'speed_elsa')

#to plot annas
plt.scatter(anna_distance_km, anna_speed_kmph, marker='+', color='orange')
plt.plot(x_anna, anna_velocity)

#to plot elsas
plt.scatter(elsa_distance_km, elsa_speed_kmph,marker='+', color='orange')
plt.plot(x_elsa, elsa_velocity, color='green')

plt.xlabel('Distance [km]')
plt.ylabel('Speed [km/h]')
plt.grid()
plt.show()