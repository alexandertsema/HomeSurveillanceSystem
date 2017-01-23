import datetime


class FileHelper(object):
    def __init__(self):
        pass

    @property
    def fileName(self):
        return datetime.datetime.now().strftime("%I-%M-%S-%f %p - %B %d %Y")
