from settings import *
import pygame
import math
from map import Map
from player import Player
def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
class Ray:
    def __init__(self):
        self.horizontal_point = None
        self.wall_horizontal_x = None
        self.wall_horizontal_y = None
        self.wall_vertical_x = None
        self.wall_vertical_y = None
        self.closest_distance = None
        self.closest_point = None
    def detect_walls(self, screen, px, py, pangle, pdx, pdy, map):
        tan = abs(math.tan(pangle))
        print("start")
        found_h = False
        h_x_counter = px
        h_y_counter = py
        if pdy == 'up':
            opposite = py % TILESIZE
            adjacent = opposite / tan
            if pdx == 'right':
                h_x_counter += adjacent
            elif pdx == 'left':
                h_x_counter -= adjacent
            h_y_counter -= opposite
            print(f"adjacent:{adjacent}")
            print(f"opposite:{opposite}")
            while found_h == False:
                print("new loop")
                if map.has_wall_at(int(h_y_counter//TILESIZE) - 1, int(h_x_counter//TILESIZE)):
                    horizontal_point = (h_x_counter, h_y_counter)
                    print(f"hp:{horizontal_point}")
                    print(int(h_x_counter//TILESIZE),int(h_y_counter//TILESIZE) - 1)
                    found_h = True 
                else:
                    h_y_counter -= TILESIZE
                    if pdx == 'right':
                        h_x_counter += TILESIZE/tan
                    elif pdx == 'left':
                        h_x_counter -= TILESIZE/tan
        pygame.draw.line(screen, (255,255,255), (px,py), (h_x_counter, h_y_counter), 2)
                
            
    def cast(self, screen, px, py, pangle):
        pygame.draw.line(screen,(0,0,255),(px, py), (self.closest_point))