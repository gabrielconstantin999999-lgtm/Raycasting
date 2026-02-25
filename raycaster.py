from settings import *
import pygame
import math
from map import Map
from player import Player


class Raycaster:
    def __init__(self):
        pass
    def cast_rays(self, screen, ray, player, map):
        for x in range(0, FOV, FOV/NUM_RAYS):
            ray.cast(screen, player.x, player.y, x, player.direction_x, player.direction_y, map)
            ray.detect_walls(screen, player.x, player.y, x)