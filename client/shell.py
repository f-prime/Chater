import socket
import record
import utils
import thread
import send
import pyaudio

class Shell:
    def __init__(self):
        self.server = ("100.1.73.128", 5555)
        self.sock = socket.socket()
    
    def main(self):
        self.sock.connect(self.server)
        thread.start_new_thread(record.record, ())
        thread.start_new_thread(self.recv, ())
        while True:
            cmd = raw_input("> ")
            if cmd == "record":
                utils.record = True
                thread.start_new_thread(record.record, ())
            elif cmd == "stop":
                utils.record = False
            
            elif cmd == "send":
                send.send(self.sock)
            
            print len(list(utils.stream))
    def recv(self):
        stream = []
        while True:
            data = self.sock.recv(1024)
            if data:
                stream.append(data)
                if "\r\n\r\n" in ''.join(stream):
                    self.playStream(''.join(stream).replace("\r\n\r\n", ''))
                    stream = []

    def playStream(self, stream):
        p = pyaudio.PyAudio()
        pout = p.open(format=pyaudio.paInt16, channels=1, rate=44600, output=True, frames_per_buffer=1024)
        print "Streaming"
        pout.write(stream)
        print "Done"

Shell().main()
