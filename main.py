import pygame
from astroquery.jplhorizons import Horizons
from astropy.time import Time
import numpy as np
import datetime
# from datetime import datetime

from constants import (
    BLACK,
    SIMULATION_START,
    WHITE,
    WIDTH, 
    HEIGHT,
)
from solar_system.solar_system import SolarSystem

# Initialization for pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont('arial', 30)
DIST_FONT = pygame.font.SysFont('arial', 16)
pygame.display.set_caption("SolarSystem")

def main():
    elapsed_time = datetime.datetime.strptime(SIMULATION_START, '%Y-%m-%d')

    run = True
    clock = pygame.time.Clock()     # To run this simulation at the same speed on every computer

    solar_system = SolarSystem(number_of_planet=4).get_solar_system()

    while run:
        clock.tick(120)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for pos, celestial_object in enumerate(solar_system, 1):
            celestial_object.move_objects(solar_system)
            celestial_object.draw(WIN)
            text = '{}: {} AU'.format(
                celestial_object.get_object_name(), 
                celestial_object.get_distance_from_sun(),
            )
            distance_text = DIST_FONT.render(text, 1, WHITE)
            WIN.blit(distance_text, (0, 990 - pos * 40))
        elapsed_time += datetime.timedelta(days=1)
        time_text = FONT.render('Date: {}'.format(elapsed_time.strftime('%d-%m-%Y')), 1, WHITE)
        WIN.blit(time_text, (0, 0))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
