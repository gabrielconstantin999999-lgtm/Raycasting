import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.128"
        self.port = 52000
        self.addr = (self.server,self.port)
    def send(self,data):
        self.client.send(pickle.dumps(data))
    def receive(self):
        return self.client.recv(pickle.loads(4096))
    