from Particle import *


def evolve_posvel(particle, deltaT, m, particle_dict):
    """
    Evolves the system by updating position, velocity and acceleration of a particle by a single time step.

    :param particle: An object of the Particle.py Particle class
    :param deltaT: The length of time to update the system by (float value)
    :param m: The method of updating to use (either 'Euler' or 'EulerCromer') (string value)
    :param particle_dict: A dictionary of all Particle objects in the current system

    :return: A copy of the particle object with updated position, velocity and acceleration
    """
    # Define new dictionary without original particle

    dict_wo_particle = {}
    for x in particle_dict.keys():
        if particle_dict[x] != particle:
            dict_wo_particle[x] = particle_dict[x]

    accel = np.array([0, 0, 0], dtype=float)
    for obj in dict_wo_particle.values():
        accel += particle.updateGravitationalAcceleration(obj)
    particle.acceleration = accel

    # Update based on chosen method
    if m == "Euler":
        particle.update_euler(deltaT)
    elif m == "EulerCromer":
        particle.update_eulerCromer(deltaT)

    return particle


def evolve_energy(particle, deltaT, m, particle_dict):
    """
    Evolves the system by updating position, velocity and acceleration of a particle by a single time step.
    Calculates total energy of the particle after updating (kinetic + potential).

    :param particle: An object of the Particle.py Particle class
    :param deltaT: The length of time to update the system by (float value)
    :param m: The method of updating to use (either 'Euler' or 'EulerCromer') (string value)
    :param particle_dict: A dictionary of all Particle objects in the current system

    :return: A copy of the particle object with updated position, velocity and acceleration
             The float value of the particle's total energy after updating
    """

    # Define new dictionary without original particle

    dict_wo_particle = {}
    for x in particle_dict.keys():
        if particle_dict[x] != particle:
            dict_wo_particle[x] = particle_dict[x]

    accel = np.array([0, 0, 0], dtype=float)
    for obj in dict_wo_particle.values():
        accel += particle.updateGravitationalAcceleration(obj)
    particle.acceleration = accel

    # Update based on chosen method
    if m == "Euler":
        particle.update_euler(deltaT)
    elif m == "EulerCromer":
        particle.update_eulerCromer(deltaT)

    # Calculate total energy of particle

    energy = particle.kineticEnergy()
    for obj in dict_wo_particle.values():
        energy += particle.potentialEnergy(obj)
    return particle, energy


def evolve_momentum(particle, deltaT, m, particle_dict):
    """
    Evolves the system by updating position, velocity and acceleration of a particle by a single time step.
    Calculates the momentum vector of the particle after updating.

    :param particle: An object of the Particle.py Particle class
    :param deltaT: The length of time to update the system by (float value)
    :param m: The method of updating to use (either 'Euler' or 'EulerCromer') (string value)
    :param particle_dict: A dictionary of all Particle objects in the current system

    :return: A copy of the particle object with updated position, velocity and acceleration
             The momentum vector of the particle after updating
    """
    
    # Define new dictionary without original particle

    dict_wo_particle = {}
    for x in particle_dict.keys():
        if particle_dict[x] != particle:
            dict_wo_particle[x] = particle_dict[x]

    accel = np.array([0, 0, 0], dtype=float)
    for obj in dict_wo_particle.values():
        accel += particle.updateGravitationalAcceleration(obj)
    particle.acceleration = accel

    # Update based on chosen method
    if m == "Euler":
        particle.update_euler(deltaT)
    elif m == "EulerCromer":
        particle.update_eulerCromer(deltaT)

    # Calculate x, y, z momentum of particle
    momentum = particle.momentum()
    return particle, momentum

# Console error message if script is run directly
if __name__ == "__main__":
    print("This python script is not intended to be run independently.\n")
    input("Press the enter key to continue")
