# Import Library
from djitellopy import Tello

# Drone Setup
drone = Tello()
drone.connect()

# Get the battery data
battery = drone.get_battery()
print(battery)
