# Import Library
from djitellopy import Tello

# Tello Setup
drone = Tello()
drone.connect()

# Take off
drone.takeoff()

# Rotate clockwise 90 degree
drone.rotate_clockwise(90)

# Rotate counter clockwise 180 degree
drone.rotate_counter_clockwise(180)

# Landing
drone.land()
