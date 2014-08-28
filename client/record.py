import pyaudio
import utils


def record():
    p = pyaudio.PyAudio()
    pin = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    
    while utils.record:
        data = pin.read(1024)
        utils.stream += data



