# TEST FILE TO TEST THE PRODUCTION OF AN EARTH-SUN-MARS POSITION PLOT

import commandFuncs as cmd
from astropy.time import Time

# Define original time (constant)
T0 = Time("2021-11-28 00:00:00.0", scale="tdb")

# Create dict of particles
particles = {}

# Initialise system with Sun & Earth
sun = cmd.add_particle('sun', T0)
earth = cmd.add_particle('earth', T0)
particles['sun'] = sun
particles['earth'] = earth

# Add Mars
mars = cmd.add_particle('mars', T0)
particles['mars'] = mars

# Create plot of orbits
cmd.plot_system(200, 500000, 'EulerCromer', particles)