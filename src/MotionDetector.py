import cv2 as cv


class MotionDetector(object):
    def __init__(self, background_model, sensitivity):
        self.sensitivity = sensitivity
        self.background_model = background_model
        pass

    def detect(self, processed_frame):
        delta = cv.absdiff(self.background_model, processed_frame)
        threshold = cv.threshold(delta, 25, 255, cv.THRESH_BINARY)[1]
        image, contours, hierarchy = cv.findContours(threshold.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            #print("ALARM")
            return self.getBoundingBox(contours)
        else:
            pass

    def getBoundingBox(self, contours):
        boxes = []
        for contour in contours:
            if cv.contourArea(contour) > self.sensitivity:
                boxes.append(cv.boundingRect(contour))
        return boxes
