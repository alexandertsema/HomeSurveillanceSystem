import threading
import time
from src.AudioManager import AudioManager
from src.FileHelper import FileHelper
from src.MergeManager import MergeManager
from src.VideoManager import VideoManager


recording = True
delay = 0
record_length = 30
video_format = "avi"
audio_format = "wav"

file_helper = FileHelper()
merge_manager = MergeManager(video_format, audio_format, file_helper)
video_manager = VideoManager(record_length, video_format)
audio_manager = AudioManager(record_length, audio_format)

time.sleep(delay)

while recording:
    file_name = file_helper.fileName
    video_manager.startRecording(file_name)
    audio_manager.startRecording(file_name)

    # time.sleep(video_length)
    #
    # video_manager.stopRecording()
    # audio_manager.stopRecording()

    while threading.active_count() > 4:
        pass

    merge_manager.merge(file_name)

    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     video_manager.stopRecording()
    #     audio_manager.stopRecording()
    #     recording = False
    #     break
