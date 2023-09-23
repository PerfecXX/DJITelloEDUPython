# Import Library
from djitellopy import Tello

# drone Setup
drone = Tello()
drone.connect()

# Takeoff
drone.takeoff()

# Get the height in cm
height = drone.get_height()
print('Height: ',height,' cm')

# Landing
drone.land()


