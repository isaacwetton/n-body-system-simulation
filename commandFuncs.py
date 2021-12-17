from Particle import *
from astropy.coordinates import get_body_barycentric_posvel
from spiceypy import sxform, mxvg
from poliastro import constants
from astropy.constants import G
import systemEvolution as evolve
from matplotlib import pyplot as plt

def add_particle(particle, t):
    """
    Adds a new particle from a pre-defined list, including the ability to add custom particles

    :param particle: The name of the particle to add. Can be the name of a planet in the solar system or 'custom'
                     to create a custom particle. (string)
    :param t: The time at which to retrieve ephemeris data for. (astropy Time object)

    :return: A Particle.py Particle object that corresponds with the inputted particle parameter.
    """
    if particle in ('sun', 'mercury', 'venus', 'earth', 'mars',
                    'jupiter', 'saturn', 'uranus', 'neptune', 'pluto'):
        # Retrieve initial position and velocity
        pos, vel = get_body_barycentric_posvel(particle, t, ephemeris="jpl")

        statevec = [
            pos.xyz[0].to("m").value,
            pos.xyz[1].to("m").value,
            pos.xyz[2].to("m").value,
            vel.xyz[0].to("m/s").value,
            vel.xyz[1].to("m/s").value,
            vel.xyz[2].to("m/s").value,
        ]

        # get transformation matrix to the ecliptic (use time in Julian Days)
        trans = sxform("J2000", "ECLIPJ2000", t.jd)

        # transform state vector to ecliptic
        statevececl = mxvg(trans, statevec, 6, 6)

        # get positions and velocities
        pos = [statevececl[0], statevececl[1], statevececl[2]]
        vel = [statevececl[3], statevececl[4], statevececl[5]]

        # retrieve correct mass
        particle_mass = mass[particle]
    elif particle == 'custom':
        print('What is the name of the object?')
        particle = input('')
        while particle in ('sun', 'mercury', 'venus', 'earth', 'mars',
                           'jupiter', 'saturn', 'uranus', 'neptune', 'pluto'):
            print('Invalid name. Enter a valid particle name:')
            particle = input('')
        print("What is the mass of the particle (kg)?")
        particle_mass = float(input(''))
        print('What is the initial position vector (in form x,y,z)?')
        pos_str = input('').split(',')
        pos = [float(pos_str[0]), float(pos_str[1]), float(pos_str[2])]
        print('What is the initial velocity vector (in form x,y,z)?')
        vel_str = input('').split(',')
        vel = [float(vel_str[0]), float(vel_str[1]), float(vel_str[2])]
    return Particle(name=particle, mass=particle_mass, position=pos, velocity=vel)


def del_particle(particle, particle_dict):
    """
    Deletes a currently existing particle

    :param particle: The name of the particle that is to be deleted (string)
    :param particle_dict: The dictionary of current particles (dict)
    """

    if particle in particle_dict.keys():
        particle_dict.pop(particle, None)
        print("Particle '" + particle + "' successfully deleted.")
    else:
        print("Particle '" + particle + "' does not exist.")


def plot_system(deltaT, N, m, particle_dict):
    """
    Collects data for and generates a plot of position for current particles in the system.

    :param deltaT: The time step between system evolutions (float)
    :param N: The number of system evolutions (integer)
    :param m: The method of updating to use ('Euler' or 'EulerCromer') (string)
    :param particle_dict: The dictionary of current particles (dict)
    """

    # Initialise Dictionaries
    x_values = {}
    y_values = {}
    for name in particle_dict.keys():
        x_values[name] = []
        y_values[name] = []

    for i in range(N):
        particle_dict_copy = particle_dict.copy()
        for particle in particle_dict.values():
            evolved_particle = evolve.evolve_posvel(particle, deltaT, m, particle_dict_copy)
            x_values[particle.name].append(evolved_particle.position[0])
            y_values[particle.name].append(evolved_particle.position[1])
            particle_dict[particle.name] = evolved_particle
    for name in particle_dict.keys():
        plt.plot(x_values[name], y_values[name], label=name)
    plt.xlabel("x position")
    plt.ylabel("y position")
    plt.legend(loc="upper right")
    plt.show()


def plot_energy(deltaT, N, m, particle_dict, n):
    """
    Collects data for and generates a plot of total system energy against time

    :param deltaT: The time step between system evolutions (float)
    :param N: The number of system evolutions (integer)
    :param m: The method of updating to use ('Euler' or 'EulerCromer') (string)
    :param particle_dict: The dictionary of current particles (dict)
    :param n: Data points are collected every n evolutions (integer)
    """

    time = 0
    energies = []
    times = []
    for i in range(N):
        particle_dict_copy = particle_dict.copy()
        energy = 0
        for particle in particle_dict.values():
            evolved_particle, particle_energy = evolve.evolve_energy(particle, deltaT, m, particle_dict_copy)
            energy += particle_energy
            particle_dict[particle.name] = evolved_particle
        time += deltaT
        if N % n == 0:
            energies.append(energy)
            times.append(time)
    plt.plot(times, energies, label="Total System Energy")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.legend(loc="upper right")
    plt.show()


def plot_momentum(deltaT, N, m, particle_dict, n):
    """
    Collects data for and generates a plot of total system momentum against time.
    Total momentum is given as an absolute value.
    The individual x, y, z momentums are also plotted.

    :param deltaT: The time step between system evolutions (float)
    :param N: The number of system evolutions (integer)
    :param m: The method of updating to use ('Euler' or 'EulerCromer') (string)
    :param particle_dict: The dictionary of current particles (dict)
    :param n: Data points are collected every n evolutions (integer)
    """
    time = 0
    x_moms = []
    y_moms = []
    z_moms = []
    total_moms = []
    times = []
    for i in range(N):
        particle_dict_copy = particle_dict.copy()
        x_mom = 0
        y_mom = 0
        z_mom = 0
        for particle in particle_dict.values():
            evolved_particle, particle_momentum = evolve.evolve_momentum(particle, deltaT, m, particle_dict_copy)
            x_mom = particle_momentum[0]
            y_mom = particle_momentum[1]
            z_mom = particle_momentum[2]
            total_mom = np.linalg.norm(particle_momentum)
            particle_dict[particle.name] = evolved_particle
        time += deltaT
        if N % n == 0:
            x_moms.append(x_mom)
            y_moms.append(y_mom)
            z_moms.append(z_mom)
            total_moms.append(total_mom)
            times.append(time)
    plt.plot(times, x_moms, label="Total x momentum")
    plt.plot(times, y_moms, label="Total y momentum")
    plt.plot(times, z_moms, label="Total z momentum")
    plt.plot(times, total_moms, label="Total system momentum (absolute)")
    plt.xlabel("Time (s)")
    plt.ylabel("Momentum (m.kg.s^-1)")
    plt.legend(loc="upper right")
    plt.show()

# Define masses
mass = {
    'sun': (constants.GM_sun / G).value,
    'mercury': (constants.GM_mercury / G).value,
    'venus': (constants.GM_venus / G).value,
    'earth': (constants.GM_earth / G).value,
    'mars': (constants.GM_mars / G).value,
    'jupiter': (constants.GM_jupiter / G).value,
    'saturn': (constants.GM_saturn / G).value,
    'uranus': (constants.GM_uranus / G).value,
    'neptune': (constants.GM_neptune / G).value,
    'pluto': (constants.GM_pluto / G).value
}

# Console error message if script is run directly
if __name__ == "__main__":
    print("This python script is not intended to be run independently.\n")
    input("Press the enter key to continue")
