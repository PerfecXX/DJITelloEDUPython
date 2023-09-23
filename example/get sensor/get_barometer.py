# Import Library
from djitellopy import Tello

# drone Setup
drone = Tello()
drone.connect()

# Takeoff
drone.takeoff()

# Get the barometer measurement in cm
baro = drone.get_barometer()
print(baro)

# Landing
drone.land()
