import socket 
from _thread import *
import pickle

server = "192.168.1.128"
port = 52000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server,port))

s.listen(2)
print("Waiting.")
p_info = [{},{}]
def threaded_client(conn,player):
    while True:
        data = pickle.loads(conn.recv(4096))
        if not data:
            print("Disconnected.")
            break
        else:
            if player == 1:
                p_info[0] = data
                conn.sendall(pickle.dumps(p_info[1]))
            else:
                p_info[1] = data
                conn.sendall(pickle.dumps(p_info[0]))
    print("Disconnected.")
    conn.close()


player_num = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,player_num))
    player_num += 1