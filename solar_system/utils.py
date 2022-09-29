from .celestial_constants import *

def get_position(planet_name: str) -> tuple:
    return globals()['{}_POSITION'.format(planet_name.upper())]

def get_radius(planet_name: str) -> float:
    return globals()['{}_RADIUS'.format(planet_name.upper())]

def get_initial_y_velocity(planet_name: str) -> float:
    return globals()['{}_VELOCITY'.format(planet_name.upper())]

def get_mass(planet_name: str) -> float:
    return globals()['{}_MASS'.format(planet_name.upper())]

def get_color(planet_name: str) -> tuple:
    return globals()['{}_COLOR'.format(planet_name.upper())]

def get_max_length_orbit_line(from_planet: str) -> int:
    '''
    This function return the approximation value of `from_planet` revolution around the sun in a day.
    '''
    match from_planet:
        case "Mercury":
            return 80           # Return approx. Mercury revolution duration in days, real = 87.97 days
        case "Venus":           
            return 215          # Return approx. Venus revolution duration in days, real = 224.7 days
        case "Earth":
            return 355          # Return approx. Earth revolution duration in days, real = 365 days
        case "Mars":
            return 675          # Return approx. Mars revolution duration in days, real = 686.67 days
        case "Jupiter":
            return 4_325        # Return approx. Jupiter revolution duration in days, real = 4,331.87 days
        case "Saturn":
            return 10_740       # Return approx. Saturn revolution duration in days, real = 10,752.9 days
        case "Uranus":
            return 30_665       # Return approx. Uranus revolution duration in days, real = 30,684.65 days
        case "Neptune":
            return 60_125       # Return approx. Neptune revolution duration in days, real = 60,148.35 days
    
    return 355                  # By default return approx. Earth revolution duration in days 