import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz'
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']
    return distance_km, speed_kmph


def plot_route(route):
    """
    Plots the route in given route file
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Plot scatter small dots
    plt.scatter(distance_km, speed_kmph, s=1)

    plt.xlabel('Distance (km)')
    plt.ylabel('Speed (km/h)')
    print(distance_km[-1], len(distance_km))
    plt.show()


def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)


### PART 1A ###
def consumption(v):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    # raise NotImplementedError('consumption not implemented yet!')

    return 546.8 * v ** (-1) + 50.31 + 0.2594 * v + 0.008210 * v ** 2


### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x >= 0), 'x must be non-negative'
    assert np.all(x <= distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph, x)
    return v


### PART 2A ###

def squared(x):
    return x ** 2


def integrera(f, a, b, N):
    h = (b - a) / (N - 1)
    xi = np.linspace(a, b, N)
    fi = f(xi)
    Aj = h * (fi[:-1] + fi[1:]) / 2
    return sum(Aj)


def time_to_destination(x, route, N):
    """ integrate with trapetsmetoden """

    # points = 0
    # for i in range((N - 1)):
    #    points += (1 / velocity(x / (N - 1) * i, route) + 1 / velocity(x / (N - 1) * (i + 1), route))

    # return points * (x / (N - 1) / 2) Egen metod, långsam

    h = (x - 0) / (N - 1)
    xi = np.linspace(0, x, N)
    fi = 1 / velocity(xi, route)
    Aj = h * (fi[:-1] + fi[1:]) / 2
    return sum(Aj)


### PART 2B ###
def total_consumption(x, route, N):
    # points = 0
    # for i in range((N - 1)):
    #     points += consumption(velocity(x / (N - 1) * i, route)) + consumption(velocity(x / (N - 1) * (i + 1), route))
    # return points * (x / (N - 1) / 2)

    h = (x - 0) / (N - 1)
    xi = np.linspace(0, x, N)
    fi = consumption(velocity(xi, route))
    Aj = h * (fi[:-1] + fi[1:]) / 2
    return sum(Aj)

# route = "speed_anna.npz"
# distance_km, _ = load_route(route)
# x = distance_km[-1]
# print(total_consumption(distance_km[-1], route, 10000001))
# print(total_consumption(distance_km[-1], route, 10001))


### PART 3A ###
def distance(T, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('distance not implemented yet!')


### PART 3B ###
def reach(C, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')
