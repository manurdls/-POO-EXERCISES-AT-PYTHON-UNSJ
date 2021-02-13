from claseAudioFile import AudioFile

class WavFile(AudioFile):
    __ext : str

    def __init__(self, filename):
        self.__ext = 'wav'
        super().__init__(filename)

    def getExt(self):
        return self.__ext

    def play(self):
        print('Reproduciendo {} como wav'.format(self.getFilename()))