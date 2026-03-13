import socket 
from _thread import *
import pickle

server = "192.168.1.128"
port = 52000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server,port))

s.listen(2)
print("Waiting.")
players = [None,None]
def threaded_client(conn, player_num):
    while True:
        data = pickle.loads(conn.recv(4096))
        players[player_num] = data
        try:  
            if not data:
                break
            if player_num == 1:
                reply = players[0]
            else:
                reply = players[1]
            print(players)
            conn.sendall(pickle.dumps(reply))
        except:
            break
            
    conn.close()


player_num = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,player_num))
    player_num += 1