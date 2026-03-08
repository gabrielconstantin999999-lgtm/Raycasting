import pygame
from settings import *
from map import Map
from player import Player
from ray import Ray
from raycaster import Raycaster

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
map = Map()
player1 = Player(22, 5, 9)
player2 = Player(23, 6, -9)
ray = Ray()
clock = pygame.time.Clock()
raycaster = Raycaster()

pov_switch = 9
while True:
    clock.tick(60)
    screen.fill((232, 195, 195))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pov_switch *= -1 
    
    if pov_switch == 9:
        player1.update(screen, map)
        raycaster.cast_rays(screen, ray, player1, player2, map)
    elif pov_switch == -9:
        player2.update(screen, map)
        raycaster.cast_rays(screen, ray, player2, player1, map)
    map.update()
    #map.draw(screen)
    #raycaster.cast_rays(screen, ray, player1, map)
    #ray.detect_walls(screen, player.x, player.y, player.rotation_angle, player.direction_x, player.direction_y, map)
    #ray.cast(screen, player.x, player.y, player.rotation_angle)
    #print(ray.distance)
    
    pygame.display.update()
