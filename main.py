import pygame
from settings import *
from map import Map
from player import Player
from ray import Ray

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
map = Map()
player = Player()
ray = Ray()
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    map.draw(screen)
    player.update(screen)
    ray.detect_walls(screen, player.x, player.y, player.rotation_angle, player.direction_x, player.direction_y, map)
    ray.cast(screen, player.x, player.y, player.rotation_angle)
    pygame.display.update()