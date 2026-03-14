import socket 
from _thread import *
import pickle

TILESIZE = 32
server = "192.168.1.128"
port = 52000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server,port))

s.listen(2)
print("Waiting.")
players = [[22 * TILESIZE,5 * TILESIZE],[24 * TILESIZE,7 * TILESIZE]]
def threaded_client(conn, player_num):
    while True:
        try:
            print(player_num)
            conn.sendall(pickle.dumps(players[player_num]))
            data = pickle.loads(conn.recv(4096))
            if not data:
                break
            if player_num == 0:
                players[0] = data
                reply = players[1]
            elif player_num == 1:
                players[1] = data
                reply = players[0]
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