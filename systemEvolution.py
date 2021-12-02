from Particle import *

def evolve_posvel(particle, deltaT, N, particle_dict):
    time = 0
    for i in range(N):
        for object in particle_dict.values():
            if object != particle:
                particle.updateGravitationalAcceleration(object)
        particle.update(deltaT)
        time += deltaT
    return particle.position, particle.velocity
