import socket 
from _thread import *
import pickle
import time


TILESIZE = 32
server = "192.168.1.128"
port = 52000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server,port))

s.listen(2)
print("Waiting.")



players = [[22*TILESIZE,5*TILESIZE,False],[25*TILESIZE,7*TILESIZE,False]]

healths = [100,100]

ready = [False,False]

score = [0,0]

reset = False

def threaded_client(conn, player_num):
    global reset, healths, score
    while True:
        try:
            if not ready[0] or not ready[1]:
                state = pickle.loads(conn.recv(4096))
                if state == "wait": ready[player_num] = True
                if ready[0] and ready[1]:
                    conn.sendall(pickle.dumps("game"))
                else: 
                    conn.sendall(pickle.dumps("wait"))
            if ready[0] and ready[1]:
                data = pickle.loads(conn.recv(4096))
                players[player_num] = data
                if not data:
                    break
                if player_num == 0:
                    if players[0][2] == True:
                        healths[1] -= 5
                        players[0][2] = False
                    players[0] = data
                    if healths[0] <= 0:
                        score[1] += 1
                        reset = True
                        healths = [100,100]
                    if healths[1] <= 0:
                        score[0] += 1
                        reset = True
                        healths = [100,100]
                    reply = [players[1],healths[0],[score[0],score[1]],reset]
                elif player_num == 1:
                    if players[1][2] == True:
                        healths[0] -= 5
                        players[1][2] = False
                    players[1] = data
                    if healths[0] <= 0:
                        score[1] += 1
                        reset = True
                        healths = [100,100]
                    if healths[1] <= 0:
                        score[0] += 1
                        reset = True
                        healths = [100,100]
                    reply = [players[0], healths[1],[score[1],score[0]],reset]
                print(players)
                conn.sendall(pickle.dumps(reply))
                print(healths)
                reset = False
        except socket.error as e:
            print(e)
            break
    player_num -= 1
    conn.close()


player_num = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,player_num))
    player_num += 1