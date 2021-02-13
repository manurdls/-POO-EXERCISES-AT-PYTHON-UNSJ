from claseMP3 import MP3File
from claseWavFile import WavFile
from claseOggFile import OggFile

def testAudioFile():
    musicaMP3 = MP3File('Sweet child o mine.mp3')  #cambiar extencion para entender
    musicaMP3.play()

    musicaWAV = WavFile('November rain.wav')    #cambiar extencion para entender
    musicaWAV.play()

    musicaOGG = OggFile('Civil war.ogg')    #cambiar extencion para entender
    musicaOGG.play()

if __name__ == '__main__':
    testAudioFile()