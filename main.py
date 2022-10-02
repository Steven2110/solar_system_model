import pygame
import datetime

from constants import (
    BLACK,
    SIMULATION_START,
    WHITE,
    WIDTH, 
    HEIGHT,
)
from solar_system.celestial_constants import PLANETS
from solar_system.solar_system import SolarSystem

# Initialization for pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
FONT = pygame.font.SysFont('arial', 30)
DIST_FONT = pygame.font.SysFont('arial', 16)
pygame.display.set_caption("SolarSystem")

def main():
    start_time = datetime.datetime.strptime(SIMULATION_START, '%Y-%m-%d')
    current_time = datetime.datetime.strptime(SIMULATION_START, '%Y-%m-%d')

    run = True
    clock = pygame.time.Clock()     # To run this simulation at the same speed on every computer

    solar_system = SolarSystem(planets=PLANETS).get_solar_system()

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
            distance_text = DIST_FONT.render(text, 1, celestial_object.get_object_color())
            WIN.blit(distance_text, (0, 990 - pos * 40))
        current_time += datetime.timedelta(days=1)
        elapsed_time = (current_time - start_time).days
        start_time_text = FONT.render('Date start: {}'.format(start_time.strftime('%d-%m-%Y')), 1, WHITE)
        current_time_text = FONT.render('Date current: {}'.format(current_time.strftime('%d-%m-%Y')), 1, WHITE)
        elapsed_time_text = FONT.render('Run time: {} days'.format(elapsed_time), 1, WHITE)
        WIN.blit(start_time_text, (0, 0))
        WIN.blit(current_time_text, (0, 50))
        WIN.blit(elapsed_time_text, (0, 100))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
