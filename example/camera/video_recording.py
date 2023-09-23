# Import Library
import time
import cv2
import os
from threading import Thread
from djitellopy import Tello

# Drone Setup
tello = Tello("192.168.31.11")
tello.connect()

# Recording status
keepRecording = True

# Turn on video streaming
tello.streamon()

# Read the frame from video streaming
frame_read = tello.get_frame_read()

# Get the current date as the timestamp
timestamp = time.strftime("%Y-%m-%d")

# Initialize a global file_number variable
file_number = 1

def videoRecorder():
    global file_number  # Declare file_number as a global variable
    height, width, _ = frame_read.frame.shape

    while keepRecording:
        # Construct the video file name
        video_filename = f"VDO_{timestamp}_{file_number}.mp4"

        # Check if the file already exists
        if os.path.exists(video_filename):
            file_number += 1
            continue  # Skip this iteration and check the next file number

        # Create a VideoWriter object to save the video as the constructed filename using the H.264 codec
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(video_filename, fourcc, 30, (width, height))
        
        # Recording the video from the image frame
        while keepRecording:
            video.write(frame_read.frame)
            time.sleep(1 / 30)
        
        # release the video writer
        video.release()
        file_number += 1  # Increment the global file number

# Start a new thread for recording video
recorder = Thread(target=videoRecorder)
recorder.start()

# Takeoff 
tello.takeoff()

# Any Drone Action
tello.rotate_counter_clockwise(360)

# Landing
tello.land()

# Stop recording
keepRecording = False
recorder.join()

