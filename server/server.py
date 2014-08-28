import socket
import json
import thread

class Server:
    def __init__(self):
        self.host = ("0.0.0.0", 5555)
        self.online = []
        self.sock = socket.socket()

    def main(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.host)
        self.sock.listen(5)
        while True:
            obj, conn = self.sock.accept()
            print conn[0]
            self.online.append(obj)
            thread.start_new_thread(self.handle, (obj,))
    
    def handle(self, obj):
        stream = []
        while True:
            data = obj.recv(1024)
            if not data:
                continue
                print 'a'
            stream.append(data)
            if "\r\n\r\n" in ''.join(stream):
                self.send(obj, ''.join(stream))
                stream = []
                print stream

    def send(self, obj, data):
        for x in self.online:
            if x != obj:
                try:
                    x.send(data)
                except:
                    self.online.remove(x)



Server().main()
