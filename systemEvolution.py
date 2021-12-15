from Particle import *


def evolve_posvel(particle, deltaT, m, particle_dict):

    # Define new dictionary without original particle

    dict_wo_particle = {}
    for x in particle_dict.keys():
        if particle_dict[x] != particle:
            dict_wo_particle[x] = particle_dict[x]

    x = []
    y = []
    accel = np.array([0, 0, 0], dtype=float)
    for obj in dict_wo_particle.values():
        accel += particle.updateGravitationalAcceleration(obj)
    particle.acceleration = accel

    # Update based on chosen method
    if m == "Euler":
        particle.update_euler(deltaT)
    elif m == "EulerCromer":
        particle.update_eulerCromer(deltaT)

    return particle.position[0], particle.position[1]

def evolve_energy(particle, deltaT, N, m, particle_dict, n):
    time = 0

    # Define new dictionary without original particle

    dict_wo_particle = {}
    for x in particle_dict.keys():
        if particle_dict[x] != particle:
            dict_wo_particle[x] = particle_dict[x]

    for i  in range(N):
        accel = np.array([0, 0, 0], dtype=float)
        for object in dict_wo_particle.values():
            accel += particle.updateGravitationalAcceleration(object)
        particle.acceleration = accel

        # Update based on chosen method
        if m == "Euler":
            particle.update_euler(deltaT)
        elif m == "EulerCromer":
            particle.update_eulerCromer(deltaT)
        time += deltaT

        # Calculate total energy within system

        energy = 0
