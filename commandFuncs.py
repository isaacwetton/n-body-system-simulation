from Particle import *
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from spiceypy import sxform, mxvg
from poliastro import constants
from astropy.constants import G

def add_particle(particle, t):
    if particle in ('sun', 'mercury', 'venus', 'earth', 'moon', 'mars',
                    'jupiter', 'saturn', 'uranus', 'neptune', 'pluto'):
        # Retrieve initial position and velocity
        pos, vel = get_body_barycentric_posvel("sun", t, ephemeris="jpl")

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

# Define masses
mass = {
    'sun': (constants.GM_sun / G).value,
    'mercury': (constants.GM_mercury / G).value,
    'venus': (constants.GM_venus / G).value,
    'earth': (constants.GM_earth / G).value,
    'moon': (constants.GM_moon / G).value,
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
