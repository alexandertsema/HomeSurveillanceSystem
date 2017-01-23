import subprocess
import threading


class MergeManager(object):
    def __init__(self, video_format, audio_format, file_helper):
        self.video_format = video_format
        self.audio_format = audio_format
        self.file_helper = file_helper
        self.thread = None
        pass

    def merge(self, file_name):
        self.thread = threading.Thread(target=self.mergeDelegate, args=[file_name])
        self.thread.start()

    def mergeDelegate(self, file_name):
        input_video_file_name = f"tmp_{file_name}.{self.video_format}"
        input_audio_file_name = f"tmp_{file_name}.{self.audio_format}"
        print(f"Merging {input_video_file_name} and {input_audio_file_name} into {file_name}.{self.video_format}...")
        cmd = f"ffmpeg -ac 2 -channel_layout stereo -i {input_audio_file_name} -i {input_video_file_name} -pix_fmt yuv420p {file_name}.{self.video_format}"
        subprocess.call(cmd, shell=True)
        print("Successfully merged")
        self.file_helper.deleteFile(input_video_file_name)
        self.file_helper.deleteFile(input_audio_file_name)
        pass

