# Import Library
import cv2
from djitellopy import Tello
import os

# Tello Setup
tello = Tello()
tello.connect()

# Turn on video streaming
tello.streamon()

# Takeoff
tello.takeoff()

# Take a photo
frame = tello.get_frame_read().frame

# Get the current date for the filename
current_date = time.strftime("%Y-%m-%d")

# Find the next available file number
file_number = 1
while os.path.exists(f"IMG_{current_date}_{file_number}.jpg"):
    file_number += 1

# Create the filename
filename = f"IMG_{current_date}_{file_number}.jpg"

# Save the photo
cv2.imwrite(filename, frame)
print(f"Photo saved as {filename}")

# Landing
tello.land()


