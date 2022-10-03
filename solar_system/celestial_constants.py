from constants import REAL_SCALE
# This file is used to store all constants value that related with planets

# Name of all planets in solar system

PLANETS = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune'
]

# Color for all celestial objects in RGB
SUN_COLOR = (255, 255, 255)
MERCURY_COLOR = (173, 168, 165)
VENUS_COLOR = (227, 158, 28)
EARTH_COLOR = (79, 76, 176)
MARS_COLOR = (193, 68, 14)
JUPITER_COLOR = (216, 202, 157)
SATURN_COLOR = (234, 214, 184)
URANUS_COLOR = (225, 238, 238)
NEPTUNE_COLOR = (75, 112, 221)

# Radius for all celestial objects, we use real radius if user give `REAL_SCALE` value of `True`,
# else we use 50 value for sun and for other planet we use approx scaling from earth size.
SUN_RADIUS = 695_340_000 if REAL_SCALE else 50
MERCURY_RADIUS = 2_440_000 if REAL_SCALE else 6
EARTH_RADIUS = 6_371_000 if REAL_SCALE else 20
VENUS_RADIUS = 6_052_000 if REAL_SCALE else 19
MARS_RADIUS = 3_390_000 if REAL_SCALE else 10
JUPITER_RADIUS = 69_991_000 if REAL_SCALE else 220
SATURN_RADIUS = 58_232_000 if REAL_SCALE else 180
URANUS_RADIUS = 25_362_000 if REAL_SCALE else 80
NEPTUNE_RADIUS = 24_662_000 if REAL_SCALE else 79

# Masses for all celestial objects in Kilogram
SUN_MASS = 1.98847e30
MERCURY_MASS = 0.3285e24
VENUS_MASS = 4.867e24
EARTH_MASS = 5.9742e24
MARS_MASS = 0.642e24
JUPITER_MASS = 1898e24
SATURN_MASS = 568.3e24
URANUS_MASS = 86.81e24
NEPTUNE_MASS = 102.4e24

# Velocities in y axis for all planets in meter per second
MERCURY_VELOCITY = 47.36 * 1000
VENUS_VELOCITY = 35.02 * 1000
EARTH_VELOCITY = 29.783 * 1000
MARS_VELOCITY = 24.077 * 1000
JUPITER_VELOCITY = 13.06 * 1000
SATURN_VELOCITY = 9.68 * 1000
URANUS_VELOCITY = 6.80 * 1000
NEPTUNE_VELOCITY = 5.43 * 1000

# Pos
MERCURY_POSITION = (0.387, 0)
VENUS_POSITION = (0.723, 0)
EARTH_POSITION = (1, 0)
MARS_POSITION = (1.524, 0)
JUPITER_POSITION = (5.2, 0)
SATURN_POSITION = (9.5, 0)
URANUS_POSITION = (19.8, 0)
NEPTUNE_POSITION = (30, 0)