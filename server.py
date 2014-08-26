import socket

class Server:
    def __init__(self):
        self.online = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = ("0.0.0.0", 5555)
    def main(self):
        self.sock.bind(self.host)
        while True:
            data, obj = self.sock.recvfrom(1024)
            print obj
            if obj not in self.online:
                self.online.append(obj)

            self.send(data, obj)


    def send(self, data, obj):
        for x in self.online:
            if x != obj:
                self.sock.sendto(data, obj)


if __name__ == "__main__":
    Server().main()
