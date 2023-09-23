# Import Library
from djitellopy import Tello

# drone Setup
drone = Tello()
drone.connect()

# Takeoff
drone.takeoff()

# Move to a specific xyz position with a specific speed.
#                   x   y   z  speed
drone.go_xyz_speed(100,100,100,20)

# Landing
drone.land()
