# Import modules, constants and functions
from Particle import *
import numpy as np
import commandFuncs as cmd
from astropy.time import Time


# from astropy.coordinates import get_body_barycentric_posvel
# from spiceypy import sxform, mxvg
# from poliastro import constants
# from astropy.constants import G


def run_cmd(command):
    if command == 'help' or command[:5] == 'help ':
        print("The following is a list of valid commands with descriptions.\n\n"
              "add <particle>:\t\t\t\tAdds the specified particle to the simulation. Valid particles are: "
              "sun, mercury, venus, earth, moon, mars, jupiter, saturn, uranus, neptune, pluto\n"
              "\t\t\t\t\t\t\tIf you specify the particle as 'custom', you can specify "
              "mass, position and velocity for a custom particle.\n"
              "del <particle>:\t\t\t\tDeletes an existing particle. If a particle is not specified, "
              "the list of current particles will be printed.\n"
              "plot <deltaT> <iterations> <m>:\tGenerates a plot of the current system, generating new "
              "position/velocity/acceleration at intervals of <deltaT> seconds (float value).\n"
              "\t\t\t\t\t\t\tThe program runs for a total of <iterations> iterations (integer value).\n"
              "\t\t\t\t\t\t\t<m> is the method of updating used (either Euler or EulerCromer).")
    elif command[:3] == 'add':
        if command == 'add':
            print("Usage of 'add <particle>': Adds the specified particle to the simulation. Valid particles are: "
                  "sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto\n"
                  "If you specify the particle as 'custom', you can specify "
                  "mass, position and velocity for a custom particle.")
        elif command[:4] == 'add ':
            particle = command[4:]
            if particle in ('sun', 'mercury', 'venus', 'earth', 'mars',
                            'jupiter', 'saturn', 'uranus', 'neptune', 'pluto', 'custom'):
                particle_obj = cmd.add_particle(particle, T0)
                particles[particle_obj.name] = particle_obj
                print("Particle '" + particle_obj.name + "' added successfully")
                print(particles)  # test
            else:
                print("Invalid particle.")
                print("Usage of 'add <particle>': Adds the specified particle to the simulation. Valid particles are: "
                      "sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto\n"
                      "If you specify the particle as 'custom', you can specify "
                      "mass, position and velocity for a custom particle.")
    elif command[:3] == 'del':
        if command == 'del':
            print("Usage of 'del <particle>': Deletes an existing particle. If a particle is not specified, "
                  "the list of current particles will be printed.")
        elif command[:4] == 'del ':
            particle = command[4:]
            cmd.del_particle(particle, particles)

    elif command[:4] == 'plot':
        if command == 'plot':
            print("Usage of 'plot <deltaT> <iterations>: Generates a plot of the current system, "
                  "generating new position/velocity/acceleration at intervals of <deltaT> seconds (float value).\n"
                  "The program runs for a total of <iterations> iterations (integer value)."
                  "<m> is the method of updating used (either Euler or EulerCromer).")
        elif command[:5] == 'plot ':
            args = command.split(" ")
            deltaT = float(args[1])
            iterations = int(args[2])
            m = args[3]
            cmd.plot_system(deltaT, iterations, m, particles)
            input("Plot complete, press the enter key to exit the program.\n")
            exit()

# Define list of commands
COMMANDS = ("help", "add", "del", "plot")

# Define original time (constant)
T0 = Time("2021-11-28 00:00:00.0", scale="tdb")

# Create dict of particles
particles = {}

# Initialise system with Sun & Earth
sun = cmd.add_particle('sun', T0)
earth = cmd.add_particle('earth', T0)
particles['sun'] = sun
particles['earth'] = earth

# cmd.plot_energy(100, 50000, "EulerCromer", particles, 500) # test
# Print welcome message
print("Welcome to this n-body gravity simulation by Isaac Wetton.\n\n"
      "The program initially has the Sun and Earth as the only objects.\n"
      "It uses an initial time of 00:00:00 on 2021-11-28\n\n"
      "Type 'help' for a list of commands.\n")

# Wait for user input
command = input("")

# Check for valid command
while command != "exit":
    while command[:4] not in COMMANDS and command[:3] not in COMMANDS:
        if command == "exit":
            break
        print("That is not a valid command. Type 'help' for a list of commands.")
        command = input("")
    if command == "exit":
        break
    run_cmd(command)
    command = input("")

exit()
