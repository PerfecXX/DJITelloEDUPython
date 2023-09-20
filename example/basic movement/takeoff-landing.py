# Import Library
from djitellopy import Tello

# Tello Setup
tello = Tello()
tello.connect()

# Take off
tello.takeoff()

# Landing
tello.land()
