import utils

def send(sock):
    sock.send(utils.stream+"\r\n\r\n")
    utils.stream = ""
    print "Sent"
