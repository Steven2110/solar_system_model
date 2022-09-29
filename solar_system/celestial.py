import pygame
import math

from constants import (
    AU,
    G,
    HEIGHT,
    SCALE,
    TIMESTEP,
    WIDTH,
)
from solar_system.utils import get_max_length_orbit_line


class Celestial:
    def __init__(
        self, 
        name: str, 
        x: float, 
        y: float, 
        radius: int,
        color: tuple, 
        mass: float, 
        x_velocity: float = 0.0,
        y_velocity: float = 0.0, 
        is_sun: bool = False,
    ) -> None:
        '''
        To initialize our celestial object/body, we need to pass
        it's `name`, position in `x` axis, position in `y` axis, `radius`, `color`, and `mass`.
        
        If we are initializing a star/sun we need to pass a boolean `True` to parameter `is_sun`
        '''
        self.__name = name
        self.__color = color

        self.__x = x * AU
        self.__y = y * AU

        self.__radius = radius
        self.__mass = mass

        self.__x_velocity = 0
        self.__y_velocity = y_velocity

        self.__distance_to_sun = 0

        self.__is_sun = is_sun

        self.__orbit = []

    def get_is_sun(self) -> bool:
        '''
        Getter for `is_sun`
        '''
        return self.__is_sun

    def get_mass(self) -> bool:
        '''
        Getter for `mass`
        '''
        return self.__mass

    def get_position(self) -> tuple:
        '''
        This method return the Celestial object's position in a `tuple` `(x, y)`.
        '''
        return (self.__x, self.__y)

    def get_distance_from_sun(self) -> float:
        return round(self.__distance_to_sun / AU, 4)

    def get_object_name(self) -> str:
        return self.__name

    def gravitational_force(self, other_celestial_object):
        '''
        This method is used to calculate the gravitational force between this celestial object, 
        and `other_celestial_object`. It will return the gravitational force on the x and y axis as a tuple.

        Newton's universal law of gravity:
        F = G * M * m / r²
        '''
        # Calculate the distance between 2 celestial objects using pythagorean theorem
        other_x, other_y = other_celestial_object.get_position()
        distance_x = other_x - self.__x
        distance_y = other_y - self.__y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other_celestial_object.get_is_sun():
            self.__distance_to_sun = distance

        # Find the Force of gravity by using Newton's universal law of gravity
        force = G * self.__mass * other_celestial_object.get_mass() / distance ** 2
        
        # Divide the force in x and y axis by using trigonometry ratios
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def move_objects(self, planets):
        '''
        This method is used to move the celestial objects by calculating it's `gravitational_force`, 
        then 
        '''
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.gravitational_force(planet)
            total_fx += fx
            total_fy += fy
        
        self.__x_velocity += total_fx / self.__mass * TIMESTEP      # F = m * a -> a = F / m -> v = a * ∂t
        self.__y_velocity += total_fy / self.__mass * TIMESTEP

        self.__x += self.__x_velocity * TIMESTEP
        self.__y += self.__y_velocity * TIMESTEP

        if len(self.__orbit) > get_max_length_orbit_line(from_planet=self.__name):
            self.__orbit.pop(0)
        self.__orbit.append((self.__x, self.__y))

    def draw(self, win): 
        x = self.__x * SCALE + WIDTH / 2
        y = self.__y * SCALE + HEIGHT / 2

        if len(self.__orbit) > 3:
            updated_points = []
            for point in self.__orbit:
                x_point, y_point = point
                x_point = x_point * SCALE + WIDTH / 2
                y_point = y_point * SCALE + HEIGHT / 2

                updated_points.append((x_point, y_point))
        
            pygame.draw.lines(win, self.__color, False, updated_points, 2)

        

        pygame.draw.circle(win, self.__color, (x, y), self.__radius)