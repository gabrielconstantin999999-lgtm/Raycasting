import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.128"
        self.port = 52000
        self.addr = (self.server,self.port)
        self.client.connect(self.addr)
    def send(self,data):
        self.client.sendall(pickle.dumps(data))
    def receive(self):
        return pickle.loads(self.client.recv(4096))
    

