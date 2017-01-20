from threading import Timer
import cv2 as cv
import datetime
import time
from recordingState import RecordingState

# const
delay = 3
videoLength = 10
device = 0
codec = 'XVID'
resolution = (640, 480)
frameRate = 20

# init system with delay
time.sleep(delay)

cap = cv.VideoCapture(device)
fourcc = cv.VideoWriter_fourcc(*codec)

recordingState = RecordingState(True)
recording = True

# save very first frame
ret, frame = cap.read()

background_model = None

while recording:
    # create new file
    recordingState.startRecording()
    timer = Timer(videoLength + 4, recordingState.endRecording)
    timer.start()
    fileName = datetime.datetime.now().strftime("%I-%M-%S %p - %B %d %Y") + ".avi"
    out = cv.VideoWriter(fileName, fourcc, frameRate, resolution)

    while cap.isOpened() & recordingState.state:
        ret, frame = cap.read()
        if ret:

            frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frameGray = cv.GaussianBlur(frameGray, (21, 21), 0)

            if background_model is None:
                background_model = frameGray
                continue

            # motion detection
            delta = cv.absdiff(background_model, frameGray)
            threshold = cv.threshold(delta, 25, 255, cv.THRESH_BINARY)[1]
            image, contours, hierarchy = cv.findContours(threshold.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

            # loop over the contours
            for c in contours:

                # if cv.contourArea(c) < args["min_area"]:
                #     continue

                # compute the bounding box for the contour, draw it on the frame
                (x, y, w, h) = cv.boundingRect(c)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Occupied"

            # display date
            cv.putText(frame, datetime.datetime.now().strftime("%I:%M:%S:%f %p %B %d %Y"), (10, frame.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            # write to file
            out.write(frame)

            # show stream
            cv.imshow('frame', frame)

            # kill system
            if cv.waitKey(1) & 0xFF == ord('q'):
                recording = False
                break
        else:
            break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
