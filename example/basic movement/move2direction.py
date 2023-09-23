# Import Library
from djitellopy import Tello

# Tello Setup
drone = Tello()
drone.connect()

# Takeoff
drone.takeoff()

# Move up 20 cm
drone.move_up(20)

# Move down 20 cm
drone.move_down(20)

# Move left 20 cm
drone.move_left(20)

# Move right 20 cm
drone.move_right(20)

# Move forward 20 cm
drone.move_forward(20)

# Move backward 20 cm
drone.move_back(20)

# Landing
drone.land()

