import socket

class Server:
    def __init__(self):
        self.online = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = ("localhost", 1024)
    def main(self):
        self.sock.bind(self.host)
        while True:
            data, obj = self.sock.recvfrom(1024)
            if obj not in self.online:
                self.online.append(obj)

            self.send(data, obj)


    def send(self, data, obj):
        for x in self.online:
            if x != obj:
                self.sock.sendto(data, obj)


if __name__ == "__main__":
    Server().main()
