import threading
import pyaudio
import wave


class AudioManager(object):
    def __init__(self):
        self.recording = True
        self.rate = 44100
        self.frames_per_buffer = 1024
        self.channels = 2
        self.audio_thread = None
        self.format = pyaudio.paInt16
        self.file_name = None
        self.audio = None
        self.stream = None
        self.audio_frames = []

        pass

    @property
    def fileName(self):
        return self.file_name + ".wav"

    def startRecording(self, file_name):
        self.file_name = file_name
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.frames_per_buffer)
        self.stream.start_stream()
        self.recording = True

        self.audio_thread = threading.Thread(target=self.recordingAudioDelegate)
        self.audio_thread.start()
        pass

    def stopRecording(self):
        if self.open:
            self.recording = False

            waveFile = wave.open(self.fileName, 'wb')
            waveFile.setnchannels(self.channels)
            waveFile.setsampwidth(self.audio.get_sample_size(self.format))
            waveFile.setframerate(self.rate)
            waveFile.writeframes(b''.join(self.audio_frames))
            waveFile.close()

            self.dispose()
        pass

    def dispose(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        self.audio_frames = []
        # if self.audio_thread._is_stopped:
        #     self.audio_thread.stop()
        pass

    def recordingAudioDelegate(self):
        while self.recording:
            data = self.stream.read(self.frames_per_buffer)
            self.audio_frames.append(data)
        pass
