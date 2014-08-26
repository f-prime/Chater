import socket
import thread

class Server:
    def __init__(self):
        self.frames = []
        self.online = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = ("0.0.0.0", 5555)
    def main(self):
        self.sock.bind(self.host)
        thread.start_new_thread(self.send, ())
        while True:
            data, obj = self.sock.recvfrom(1024 * 2 * 2)
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
                    if x != obj:
                        self.sock.sendto(data, obj)


if __name__ == "__main__":
    Server().main()
