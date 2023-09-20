# Import Library
from djitellopy import Tello

# Tello Setup
tello = Tello()
tello.connect()

# Takeoff
tello.takeoff()

# Move up 20 cm
tello.move_up(20)

# Move down 20 cm
tello.move_down(20)

# Move left 20 cm
tello.move_left(20)

# Move right 20 cm
tello.move_right(20)

# Move forward 20 cm
tello.move_forward(20)

# Move backward 20 cm
tello.move_back(20)

# Landing
tello.land()

