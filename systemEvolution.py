from Particle import *


def evolve_posvel(particle, deltaT, m, particle_dict):
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
