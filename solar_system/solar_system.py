import numpy as np

from solar_system.celestial import Celestial
from solar_system.celestial_constants import *
from solar_system.utils import get_color, get_mass, get_position, get_radius


class SolarSystem:  
    def __init__(self, planets) -> None:
        '''
        To initialize our solar system, we need to pass `number_of_planet` that we want to simulate.
        
        The recommended value of `number_of_planet` is 4, because more then 4 planets simulated, we need a bigger screen.

        The maximum value of `number_of_planet` is 8, because there are only 8 planets in our solar system.
        '''
        self.solar_system = []
        
        # Initialize sun and add it into first element of solar system
        self.solar_system.append(self.sun_init())

        # Initialize planets according to the number of planet passed
        for planet_name in planets:
            planet = self.planet_init(planet_name)
            self.solar_system.append(planet)
      
    def sun_init(self) -> Celestial:
        sun = Celestial(
            name='Sun',
            x=0,
            y=0,
            radius=SUN_RADIUS,
            color=SUN_COLOR,
            mass=SUN_MASS,
            is_sun=True,
        )
        return sun

    def planet_init(self, name) -> Celestial:
        # Get the initial velocity in y axis for each planet
        x_pos, y_pos = get_position(planet_name=name)

        if float(x_pos) > 0.0:
            y_velocity = globals()['{}_VELOCITY'.format(name.upper())] * -1
        else:
            y_velocity = globals()['{}_VELOCITY'.format(name.upper())]

        # Initialize planet
        planet = Celestial(
            name=name,
            x=x_pos,
            y=y_pos,
            radius=get_radius(planet_name=name),
            y_velocity=y_velocity,
            color=get_color(planet_name=name),
            mass=get_mass(planet_name=name),
        )
        return planet

    def get_solar_system(self) -> list:
        '''
        This method return the initialized solar system as a `list` of `Celestial`.
        '''
        return self.solar_system