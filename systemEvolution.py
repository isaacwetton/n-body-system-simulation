from Particle import *

def evolve_posvel(particle, deltaT, N, particle_dict):
    time = 0

    # Define new dictionary without original particle

    dict_wo_particle = {}
    for x in particle_dict.keys():
        if particle_dict[x] != particle:
            dict_wo_particle[x] = particle_dict[x]

    x = []
    y = []
    for i in range(N):
        accel = np.array([0, 0, 0], dtype=float)
        for object in dict_wo_particle.values():
            accel += particle.updateGravitationalAcceleration(object)
        particle.acceleration = accel
        particle.update_euler(deltaT)
        time += deltaT
        x.append(particle.position[0])
        y.append(particle.position[1])
    return x, y
