from settings import *
import pygame
import math
from map import Map
from player import Player

class Ray:
    def __init__(self):
        self.wall_horizontal = None
    def detect_walls(self, screen, px, py, pangle, pd):
        found_horizontal = False
        if pd == 'up':
            x_horizontal = math.tan(pangle) * (py % TILESIZE)
            y_horizontal = py // TILESIZE
            while found_horizontal == False:
                closest_horizontal_point = x_horizontal, y_horizontal
                if map.has_wall_at(y_horizontal // TILESIZE - 1, x_horizontal//TILESIZE):
                    self.wall_horizontal = closest_horizontal_point
                    found_horizontal = True
                else:
                    y_horizontal -= TILESIZE


        if pd == 'down':
            x_horizontal = math.tan(pangle) * ((py / TILESIZE + TILESIZE) % TILESIZE)
            y_horizontal = py // TILESIZE + TILESIZE
            while found_horizontal == False:
                closest_horizontal_point = x_horizontal, y_horizontal
                if map.has_wall_at((y_horizontal // TILESIZE), (x_horizontal//TILESIZE)):
                    self.wall_horizontal = closest_horizontal_point
                    found_horizontal = True
                else:
                    y_horizontal -= TILESIZE


        


    def cast(self, screen, px, py, pangle):
        pygame.draw.line(screen,(0,0,255),(px, py), (px + math.cos(pangle) * 100, self.wall_horizontal))
    