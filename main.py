# Import modules, constants and functions
from Particle import *
import numpy as np
import commandFuncs as cmd
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from spiceypy import sxform, mxvg
from poliastro import constants
from astropy.constants import G

# Define list of commands
COMMANDS = ("help", "add", "del", "plot")

# Define original time (constant)
T0 = Time("2021-11-28 00:00:00.0", scale="tdb")

# Create list of particles
particles = []

# Retrieve sun and earth positions and velocities
sunpos, sunvel = get_body_barycentric_posvel("sun", T0, ephemeris="jpl")
earthpos, earthvel = get_body_barycentric_posvel("earth", T0, ephemeris="jpl")

sunstatevec = [
    sunpos.xyz[0].to("m").value,
    sunpos.xyz[1].to("m").value,
    sunpos.xyz[2].to("m").value,
    sunvel.xyz[0].to("m/s").value,
    sunvel.xyz[1].to("m/s").value,
    sunvel.xyz[2].to("m/s").value,
]
earthstatevec = [
    earthpos.xyz[0].to("m").value,
    earthpos.xyz[1].to("m").value,
    earthpos.xyz[2].to("m").value,
    earthvel.xyz[0].to("m/s").value,
    earthvel.xyz[1].to("m/s").value,
    earthvel.xyz[2].to("m/s").value,
]
# get transformation matrix to the ecliptic (use time in Julian Days)
trans = sxform("J2000", "ECLIPJ2000", T0.jd)

# transform state vector to ecliptic
sunstatevececl = mxvg(trans, sunstatevec, 6, 6)
earthstatevececl = mxvg(trans, earthstatevec, 6, 6)

# get positions and velocities
sunpos = [sunstatevececl[0], sunstatevececl[1], sunstatevececl[2]]
sunvel = [sunstatevececl[3], sunstatevececl[4], sunstatevececl[5]]
earthpos = [earthstatevececl[0], earthstatevececl[1], earthstatevececl[2]]
earthvel = [earthstatevececl[3], earthstatevececl[4], earthstatevececl[5]]

# Retrieve Sun & Earth masses
sunmass = (constants.GM_sun / G).value
earthmass = (constants.GM_earth / G).value

# Initialise system with Sun & Earth
sun = Particle(name="Sun", position=sunpos, velocity=sunvel, mass=sunmass)
earth = Particle(name="Earth", position=earthpos, velocity=earthvel, mass=earthmass)
particles.append([sun, earth])

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
    cmd.run_cmd(command)
    command = input("")

exit()
