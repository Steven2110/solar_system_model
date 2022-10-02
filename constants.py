# This file is used to store all constants value

SIMULATION_START = "2001-12-20"     # My birthday :)

# Constants for pygame
WIDTH = 1400
HEIGHT = 990

# Constants for color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Change this value to `True` if you want to get a real scale of the simulation
REAL_SCALE = False

# Constants for solar system that can't be changed because it's the universal constants.
AU = 149_597_870_700                # 1 AU (Astronomical Unit) in meter
G = 6.67430e-11                     # Universal gravitational constant (G)

# 1 AU = 20 pixels for real scale and 1 AU = 250 for non real scale
SCALE = 20 / AU if REAL_SCALE else 250 / AU         
# Time step for simulation 1 (day) * 24 (hours) * 60 (minutes) * 60 (seconds)
TIMESTEP = 1 * 24 * 60 * 60