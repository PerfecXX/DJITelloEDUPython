# Import Library
from djitellopy import Tello

# drone Setup
drone = Tello('192.168.31.11')
drone.connect()

# Get the temperature data in Celsius.
avg_temp = drone.get_temperature()
height_temp = drone.get_highest_temperature()
low_temp = drone.get_lowest_temperature()

print('Average Temperature: ',avg_temp, ' C')
print('Height Temperature: ',height_temp, ' C')
print('Lowest Temperature: ',low_temp, ' C')
