import socket 
from _thread import *
import pickle
import pygame
import math

TILESIZE = 32
server = "192.168.1.128"
port = 52000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server,port))

s.listen(2)
print("Waiting.")

players = [[22 * TILESIZE,5 * TILESIZE,False],[24 * TILESIZE,7 * TILESIZE,False]]
healths = [[100], [100]]
def threaded_client(conn, player_num):
    while True:
        try:
            conn.sendall(pickle.dumps(players[player_num]))
            conn.sendall(pickle.dumps(healths[player_num]))
            data = pickle.loads(conn.recv(4096))
            if not data:
                break
            if player_num == 0:
                players[0] = data
                if players[0][2]:
                    healths[1][0] -= 20
                    players[0][2] = False
                reply = players[1]
            elif player_num == 1:
                players[1] = data
                if players[1][2]:
                    healths[0][0] -= 20
                    players[1][2] = False
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