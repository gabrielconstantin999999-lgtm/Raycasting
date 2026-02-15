import pygame
from settings import *
from map import Map
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
map = Map()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    map.draw(screen)
    player.update(screen)
    pygame.display.update()