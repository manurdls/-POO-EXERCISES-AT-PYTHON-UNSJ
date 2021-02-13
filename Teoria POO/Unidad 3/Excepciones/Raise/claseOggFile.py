from claseAudioFile import AudioFile

class OggFile(AudioFile):
    __ext : str

    def __init__(self, filename):
        self.__ext = 'ogg'
        super().__init__(filename)

    def getExt(self):
        return self.__ext

    def play(self):
        print('Reproduciendo {} como ogg'.format(self.getFilename()))