import threading
import time
from src.AudioManager import AudioManager
from src.FileHelper import FileHelper
from src.VideoManager import VideoManager


def stopRecording():
    video_manager.stopRecording()
    audio_manager.stopRecording()
    pass

recording = True
delay = 1
video_length = 5

file_helper = FileHelper()
video_manager = VideoManager()
audio_manager = AudioManager()

time.sleep(delay)

while recording:
    video_manager.startRecording(file_helper.fileName)
    audio_manager.startRecording(file_helper.fileName)

    time.sleep(video_length)

    video_manager.stopRecording()
    audio_manager.stopRecording()

    while threading.active_count() > 1:
        pass

    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     video_manager.stopRecording()
    #     audio_manager.stopRecording()
    #     recording = False
    #     break
