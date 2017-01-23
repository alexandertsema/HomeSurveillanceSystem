import threading
import cv2 as cv
import datetime
from src.MotionDetector import MotionDetector


class VideoManager(object):
    def __init__(self, length, video_format):
        self.video_format = video_format
        self.length = length
        self.device = 0
        self.codec = 'XVID'
        self.fourcc = cv.VideoWriter_fourcc(*self.codec)
        self.resolution = (640, 480)
        self.frame_rate = 20
        self.sensitivity = 7
        self.recording = True
        self.background_model = None
        self.cap = None
        self.motion_detector = None
        self.out = None
        self.thread = None
        self.file_name = None

    @property
    def fileName(self):
        return f"tmp_{self.file_name}.{self.video_format}"

    def startRecording(self, file_name):
        self.file_name = file_name
        self.cap = cv.VideoCapture(self.device)
        self.out = cv.VideoWriter(self.fileName, self.fourcc, self.frame_rate, self.resolution)
        self.recording = True

        self.thread = threading.Thread(target=self.recordingVideoDelegate)
        self.thread.start()
        pass

    def stopRecording(self):
        self.recording = False
        self.dispose()
        pass

    def dispose(self):
        self.out.release()
        self.cap.release()
        # cv.destroyAllWindows()
        # if self.video_thread._is_stopped:
        #     self.video_thread.stop()
        pass

    def recordingVideoDelegate(self):
        timer = threading.Timer(self.length, self.stopRecording)
        timer.start()
        while self.recording & self.cap.isOpened():
            frame = self.getFrame()
            if frame is None:
                continue
            processed_frame = self.convertToBlurryGray(frame)

            if self.background_model is None:
                self.background_model = processed_frame
                self.motion_detector = MotionDetector(self.background_model, self.sensitivity)
                continue

            bounding_boxes = self.motion_detector.detect(processed_frame)
            if bounding_boxes is not None:
                for bounding_box in bounding_boxes:
                    cv.rectangle(frame, (bounding_box[0], bounding_box[1]),
                                 (bounding_box[0] + bounding_box[2], bounding_box[1] +
                                  bounding_box[3]), (0, 255, 0), 2)

            cv.putText(frame, self.getDate(), (10, frame.shape[0] - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            if self.out is not None:
                self.out.write(frame)
                # cv.imshow('frame', frame)
        pass

    def getFrame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame

    @staticmethod
    def convertToBlurryGray(frame):
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        return cv.GaussianBlur(frame_gray, (21, 21), 0)

    @staticmethod
    def getDate():
        return datetime.datetime.now().strftime("%I:%M:%S:%f %p %B %d %Y")
