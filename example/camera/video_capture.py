# Import Library
from djitellopy import Tello
import cv2

# Drone Setup
tello = Tello()
tello.connect()

# Turn on video streaming
tello.streamon()

# Read the frame from video streaming
cap = tello.get_frame_read()

while True:
    # Get the video frame
    frame = cap.frame
    # Show the window
    cv2.imshow("Tello Video Stream", frame)
    # Press the 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Print the battery level
    print(tello.get_battery())

# Turn off the video streaming 
tello.streamoff()
# Destroy the video window
cv2.destroyAllWindows()

