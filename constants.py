# This file is used to store all constants value

SIMULATION_START = "2001-12-20"     # My birthday :)

# Constants for pygame
WIDTH = 1400
HEIGHT = 990

# Constants for color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constants for solar system
AU = 149_597_870_700                # 1 AU (Astronomical Unit) in meter
G = 6.67430e-11                     # Universal gravitational constant (G)
SCALE = 250 / AU                    # 1AU = 100 pixels
# Time step for simulation 1 (day) * 24 (hours) * 60 (minutes) * 60 (seconds)
TIMESTEP = 1 * 24 * 60 * 60