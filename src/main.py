from threading import Timer
import cv2 as cv
import time

from src.VideoManager import VideoManager


recording = True
delay = 1

video_manager = VideoManager()
time.sleep(delay)

while recording:
    timer = Timer(10, video_manager.stopRecording)
    timer.start()
    video_manager.startRecording()

    if cv.waitKey(1) & 0xFF == ord('q'):
        video_manager.dispose()
        recording = False
        break
