import pygame
from settings import *
from map import Map
from player import Player
from ray import Ray
from raycaster import Raycaster
from network import Network
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
map = Map()
player1 = Player(22, 5)
player2 = Player(25, 7)
ray = Ray()
clock = pygame.time.Clock()
raycaster = Raycaster()
n = Network()
#pov_switch = 1
while True:
    clock.tick(60)
    screen.fill((232, 195, 195))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    p_pos = n.receive()
    player1.x = p_pos[0]
    player1.y = p_pos[1]
    player1.update(screen, map)
    n.send([player1.x, player1.y])
    p2_pos = n.receive()
    if p2_pos != "Waiting for other player" and p2_pos != None:
        player2.x = p2_pos[0]
        player2.y = p2_pos[1]
    raycaster.cast_rays(screen, ray, player1, player2, map)
    print("p1",player1.x, player1.y)
    print("p2",player2.x, player2.y)



    pygame.display.update()