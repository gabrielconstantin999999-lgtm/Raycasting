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
#player2 = Player(23, 6)
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
        #if event.type == pygame.KEYDOWN:
        #   if event.key == pygame.K_p:
        #       pov_switch *= -1 
    
    player1.update(screen, map)
    n.send(player1)
    player2 = n.receive()
    raycaster.cast_rays(screen, ray, player1, player2, map)
    print("p1",player1.x, player1.y)
    print("p2",player2.x, player2.y)
    #map.draw(screen)
    #raycaster.cast_rays(screen, ray, player1, map)
    #ray.detect_walls(screen, player.x, player.y, player.rotation_angle, player.direction_x, player.direction_y, map)
    #ray.cast(screen, player.x, player.y, player.rotation_angle)
    #print(ray.distance)
    
    pygame.display.update()