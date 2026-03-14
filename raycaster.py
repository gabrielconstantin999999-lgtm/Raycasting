from settings import *
import pygame
import math
from map import Map
from player import Player

class Raycaster:
    def cast_rays(self, screen, ray, player, player2, map):
        wall_distances = []

        for x in range(int(NUM_RAYS)):
            angle = player.rotation_angle - FOV/2 + x * FOV/NUM_RAYS
            angle %= 2 * math.pi
            ray.detect_walls(player, angle, map, x)

            corrected = ray.distance * math.cos(angle - player.rotation_angle)
            wall_distances.append(corrected)

            line_height = SCREEN_H / corrected * TILESIZE
            line_width = SCREEN_W / NUM_RAYS
            color = max(0, min(255, 255 - corrected/2))

            if ray.v:
                c = min(255, int(color * 2))
                pygame.draw.rect(screen, (c, c, c), (x * line_width, SCREEN_H/2 - line_height/2, line_width, line_height))
            elif ray.h:
                pygame.draw.rect(screen, (int(color), int(color), int(color)), (x * line_width, SCREEN_H/2 - line_height/2, line_width, line_height))

        ray.detect_player(screen, player, player2, wall_distances)
        