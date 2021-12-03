from Particle import *

def evolve_posvel(particle, deltaT, N, particle_dict):
    time = 0

    # Define new dictionary without original particle

    dict_wo_particle = {}
    for x in particle_dict.keys():
        if particle_dict[x] != particle:
            dict_wo_particle[x] = particle_dict[x]

    for i in range(N):
        for object in dict_wo_particle.values():
            particle.updateGravitationalAcceleration(object)
        particle.update(deltaT)
        time += deltaT
    return particle.position, particle.velocity
