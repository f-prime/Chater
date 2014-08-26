import pyaudio
import thread
import pygame
import socket

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound
        p = pyaudio.PyAudio()
        self.pstream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.connect = ("100.1.73.128", 5555)

    def main(self):
        self.sock.connect(self.connect)
        thread.start_new_thread(self.talk, ())
        while True:
            data = self.sock.recv(1024)
            if data:
                self.sound(data).play()

    def talk(self):
        while True:
            self.sock.send(self.pstream.read(1024))


if __name__ == "__main__":
    Client().main()
