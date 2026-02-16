from settings import *
import pygame
import math
from map import Map
from player import Player

class Ray:
    def __init__(self):
        self.wall_horizontal = 100,100
    def detect_walls(self, screen, px, py, pangle, pdx, pdy, map):

        found_horizontal = False
        if pdy == 'up':
            y_horizontal = py % TILESIZE + math.floor(py)
            x_horizontal = math.tan(pangle) * (y_horizontal)
            while found_horizontal == False:
                closest_horizontal_point = x_horizontal, y_horizontal
                if map.has_wall_at(int(y_horizontal // TILESIZE - 1), int(x_horizontal//TILESIZE)) == True:
                    self.wall_horizontal = closest_horizontal_point
                    found_horizontal = True
                else:
                    y_horizontal -= TILESIZE
                    if pdx == 'right':
                        x_horizontal += math.tan(pangle) * (y_horizontal)
                    if pdx == 'left':
                        x_horizontal -= math.tan(pangle) * (y_horizontal)

        if pdy == 'down':
            y_horizontal = math.ceil(py) - py
            x_horizontal = math.tan(pangle) * (y_horizontal)
            while found_horizontal == False:
                closest_horizontal_point = x_horizontal, y_horizontal
                if map.has_wall_at(int(y_horizontal // TILESIZE), int(x_horizontal//TILESIZE)) == True:
                    self.wall_horizontal = closest_horizontal_point
                    found_horizontal = True
                else:
                    y_horizontal += TILESIZE
                    if pdx == 'right':
                        x_horizontal += math.tan(pangle) * (y_horizontal)
                    if pdx == 'left':
                        x_horizontal -= math.tan(pangle) * (y_horizontal)
        



        


    def cast(self, screen, px, py, pangle):
        pygame.draw.line(screen,(0,0,255),(px, py), (px + math.cos(pangle) * 999999999, py - math.sin(pangle) * 999999999))
    