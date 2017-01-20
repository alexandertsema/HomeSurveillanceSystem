class RecordingState(object):
    def __init__(self, state):
        self.state = state

    def endRecording(self):
        self.state = False
        pass

    def startRecording(self):
        self.state = True
        pass
