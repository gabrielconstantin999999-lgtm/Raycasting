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




players = [[22*TILESIZE,5*TILESIZE,False],[25*TILESIZE,7*TILESIZE,False]]
healths = [100,100]
def threaded_client(conn, player_num):
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player_num] = data
            if not data:
                break
            if player_num == 0:
                if players[0][2] == True:
                    healths[1] -= 5
                    players[0][2] = False
                players[0] = data
                reply = [players[1],healths[0]] 
            elif player_num == 1:
                if players[1][2] == True:
                    healths[0] -= 20
                    players[1][2] = False
                players[1] = data
                reply = [players[0], healths[1]]
            print(players)
            conn.sendall(pickle.dumps(reply))
            print(healths)
        except:
            break
            
    conn.close()


player_num = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,player_num))
    player_num += 1