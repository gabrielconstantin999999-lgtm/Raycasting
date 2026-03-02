from settings import *
import pygame
import math
from map import Map
from player import Player


class Raycaster:
    def cast_rays(self, screen, ray, player, map):
        for x in range(int(NUM_RAYS)):
            angle = player.rotation_angle - FOV/2 + x * FOV/NUM_RAYS
            angle %= 2 * math.pi
            ray.detect_walls(screen, player.x, player.y,angle,map)
            ray.cast(screen, player.x, player.y)
            distance = ray.distance
            line_height = SCREEN_H / distance * 45
            line_width = SCREEN_W / NUM_RAYS
            pygame.draw.rect(screen, (255,255,255), (x * line_width, SCREEN_H/2 - line_height/2, line_width, line_height))

