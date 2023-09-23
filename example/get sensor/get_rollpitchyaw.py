# Import Library
from djitellopy import Tello

# drone Setup
drone = Tello()
drone.connect()

# Get the data in degrees (before takeoff)
pitch = drone.get_pitch()
roll = drone.get_roll()
yaw = drone.get_yaw()

print('Pitch:',pitch,' degree')
print('Roll:',roll,' degree')
print('Yaw:',yaw,' degree')

# Takeoff
drone.takeoff()

# Get the data in degrees (hovering)
pitch = drone.get_pitch()
roll = drone.get_roll()
yaw = drone.get_yaw()

print('Pitch:',pitch,' degree')
print('Roll:',roll,' degree')
print('Yaw:',yaw,' degree')

# Rotate
drone.rotate_clockwise(90)

# Get the data in degrees (Rotate)
pitch = drone.get_pitch()
roll = drone.get_roll()
yaw = drone.get_yaw()

print('Pitch:',pitch,' degree')
print('Roll:',roll,' degree')
print('Yaw:',yaw,' degree')

# Rotate
drone.rotate_counter_clockwise(90)

# Landing
drone.land()
