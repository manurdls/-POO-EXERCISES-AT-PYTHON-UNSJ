from claseAudioFile import AudioFile

class MP3File(AudioFile):
    __ext : str

    def __init__(self, filename):
        self.__ext = 'mp3'
        AudioFile.__init__(self, filename)

    def getExt(self):
        return self.__ext

    def play(self):
        print('Reproduciendo {} como mp3'.format(self.getFilename()))