import socket
import thread

class Server:
    def __init__(self):
        self.frames = []
        self.online = []
        self.sock = socket.socket()
        self.host = ("0.0.0.0", 5555)
    def main(self):
        self.sock.bind(self.host)
        self.sock.listen(5)
        thread.start_new_thread(self.send, ())
        while True:
            obj, conn = self.sock.accept()
            thread.start_new_thread(self.recv, (obj,))

    def recv(self, obj):
        while True:
            data = obj.recv(1024)
            print obj
            if obj not in self.online:
                self.online.append(obj)

            self.frames.append((data, obj))


    def send(self):
        while True:
            if len(self.frames) > 0:
                on = self.frames.pop(0)
                data = on[0]
                obj = on[1]
                for x in self.online:
                    if obj != x:
                        x.send(data)


if __name__ == "__main__":
    Server().main()
