# Import Library
from djitellopy import Tello

# Drone Setup 
drone = Tello()
drone.connect()

# Takeoff
drone.takeoff()

# Flip
drone.flip_forward()
drone.flip_back()
drone.flip_left()
drone.flip_right()

# Landing
drone.land()

