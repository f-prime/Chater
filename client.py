import pyaudio
import thread
import socket

class Client:
    def __init__(self):
        self.frames = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        p = pyaudio.PyAudio()
        self.pstream = p.open(format=pyaudio.paInt16, channels=2, rate=44600, input=True, frames_per_buffer=1024)
        self.ostream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, frames_per_buffer=1024)
        self.connect = ("100.1.73.128", 5555)

    def main(self):
        self.sock.connect(self.connect)
        thread.start_new_thread(self.talk, ())
        thread.start_new_thread(self.stream, ())
        while True:
            data = self.sock.recv(1024 * 2 * 1000000)
            if data:
                self.ostream.write(data, 1024)

    def talk(self):
        while True:
            self.frames.append(self.pstream.read(1024))

    def stream(self):
        while True:
            if len(self.frames) > 0:
                self.sock.send(self.frames.pop(0))


if __name__ == "__main__":
    Client().main()
