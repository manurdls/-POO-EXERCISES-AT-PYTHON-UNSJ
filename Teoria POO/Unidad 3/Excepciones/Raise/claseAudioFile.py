class AudioFile(object):
    __filename : str

    def __init__(self, filename):
        if not filename.endswith(self.getExt()):
            raise Exception('Formato de audio no valido')
        self.__filename = filename

    def getFilename(self):
        return self.__filename