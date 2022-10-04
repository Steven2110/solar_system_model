# solar_system_model
Simulation of Solar System in Pygame

## Requirements
[`Python 3.10`](https://www.python.org/downloads/release/python-3100/)

## Setup to run
Install required library by entering

`pip install -r requirements.txt`

## What can you tweak from the simulation?
### From file `constants.py`:
1. Window size.
   
   If you want to change the size of the window you can change the value according to the best size for your device.
    ```python
    WIDTH = YOUR_WIDTH
    HEIGHT = YOUR_HEIGHT
    ```

2. Switch to real scale.
   
   If you want to see the real scale of this simulation then set this variable to `True`, if you want to see the best scale for the simulation (with only inner planet) then set this variable with `False`
    ```python
    REAL_SCALE = False
    ```

3. Scale. 
   
   If you want to change the scaling of simulation by yourself, then you can change the `int` value as you desire.
    ```python
    SCALE = 20 / AU if REAL_SCALE else 250 / AU
    ```

### From file `celestial_constants.py` inside the module `solar_system`:
1. Planet's mass.
   
   You can change the sun and planet's mass and see for yourselves what will happened.
   ```python
   SUN_MASS = YOUR_CELESTIAL_OBJECT_MASS 
   MERCURY_MASS = YOUR_CELESTIAL_OBJECT_MASS
   VENUS_MASS = YOUR_CELESTIAL_OBJECT_MASS 
   EARTH_MASS = YOUR_CELESTIAL_OBJECT_MASS 
   MARS_MASS = YOUR_CELESTIAL_OBJECT_MASS 
   JUPITER_MASS = YOUR_CELESTIAL_OBJECT_MASS  
   SATURN_MASS = YOUR_CELESTIAL_OBJECT_MASS
   URANUS_MASS = YOUR_CELESTIAL_OBJECT_MASS 
   NEPTUNE_MASS = YOUR_CELESTIAL_OBJECT_MASS 
   ```
2. Planet's velocity.
   
   You can change the planet's velocity and see for your self what will happened.
   ```python
   MERCURY_VELOCITY = YOUR_PLANET_VELOCITY
   VENUS_VELOCITY = YOUR_PLANET_VELOCITY
   EARTH_VELOCITY = YOUR_PLANET_VELOCITY
   MARS_VELOCITY = YOUR_PLANET_VELOCITY
   JUPITER_VELOCITY = YOUR_PLANET_VELOCITY
   SATURN_VELOCITY = YOUR_PLANET_VELOCITY
   URANUS_VELOCITY = YOUR_PLANET_VELOCITY
   NEPTUNE_VELOCITY = YOUR_PLANET_VELOCITY 
   ```
3. Planet's position in x axis.
   
   Why can't we change the y axis position, because this simulation haven't yet supported finding `__x_velocity` and `__y_velocity` from `PLANET_VELOCITY` that is not positioned in the horizons. 

   ```python
   MERCURY_POSITION = (X_AXIS_POSITION, 0)
   VENUS_POSITION = (X_AXIS_POSITION, 0)
   EARTH_POSITION = (X_AXIS_POSITION, 0)
   MARS_POSITION = (X_AXIS_POSITION, 0)
   JUPITER_POSITION = (X_AXIS_POSITION, 0)
   SATURN_POSITION = (X_AXIS_POSITION, 0)
   URANUS_POSITION = (X_AXIS_POSITION, 0)
   NEPTUNE_POSITION = (X_AXIS_POSITION, 0) 
   ```
