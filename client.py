import pyaudio
import thread
import pygame
import socket

class Client:
    def __init__(self):
        self.frames = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound
        p = pyaudio.PyAudio()
        self.pstream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)
        self.connect = ("100.1.73.128", 5555)

    def main(self):
        self.sock.connect(self.connect)
        thread.start_new_thread(self.talk, ())
        thread.start_new_thread(self.stream, ())
        while True:
            data = self.sock.recv(1024 * 2 * 10)
            if data:
                self.sound(data).play()

    def talk(self):
        while True:
            self.frames.append(self.pstream.read(1024))

    def stream(self):
        while True:
            if len(self.frames) > 0:
                self.sock.send(self.frames.pop(0))


if __name__ == "__main__":
    Client().main()
