import datetime
import os


class FileHelper(object):
    def __init__(self):
        pass

    @property
    def fileName(self):
        return datetime.datetime.now().strftime("%I-%M-%S-%f%p-%B-%d-%Y")

    @staticmethod
    def deleteFile(file_name):
        os.remove(file_name)
