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
        found_v = False
        h_x_counter = px
        h_y_counter = py
        v_x_counter = px
        v_y_counter = py
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
        if pdy == 'down':
            opposite = TILESIZE - (py % TILESIZE)
            adjacent = opposite / tan
            if pdx == 'right':
                h_x_counter += adjacent
            elif pdx == 'left':
                h_x_counter -= adjacent
            h_y_counter += opposite
            print(f"adjacent:{adjacent}")
            print(f"opposite:{opposite}")
            while found_h == False:
                print("new loop")
                if map.has_wall_at(int(h_y_counter//TILESIZE), int(h_x_counter//TILESIZE)):
                    horizontal_point = (h_x_counter, h_y_counter)
                    print(f"hp:{horizontal_point}")
                    print(int(h_x_counter//TILESIZE),int(h_y_counter//TILESIZE))
                    found_h = True 
                else:
                    h_y_counter += TILESIZE
                    if pdx == 'right':
                        h_x_counter += TILESIZE/tan
                    elif pdx == 'left':
                        h_x_counter -= TILESIZE/tan

        if pdx == 'right':
            adjacent = TILESIZE - (px % TILESIZE)
            opposite = adjacent * tan
            
            if pdy == 'up':
                v_y_counter -= opposite
            elif pdy == 'down':
                v_y_counter += opposite
            v_x_counter += adjacent
            print(f"adjacent:{adjacent}")
            print(f"opposite:{opposite}")
            while found_v == False:
                print("new loop")
                if map.has_wall_at(int(v_y_counter//TILESIZE), int(v_x_counter//TILESIZE)):
                    vertical_point = (v_x_counter, v_y_counter)
                    print(f"hp:{horizontal_point}")
                    print(int(v_x_counter//TILESIZE),int(v_y_counter//TILESIZE))
                    found_v = True 
                else:
                    v_x_counter += TILESIZE
                    if pdy == 'down':
                        v_y_counter += TILESIZE * tan
                    elif pdy == 'up':
                        v_y_counter -= TILESIZE * tan
        if pdx == 'left':
            adjacent = px % TILESIZE
            opposite = adjacent * tan
            
            if pdy == 'up':
                v_y_counter -= opposite
            elif pdy == 'down':
                v_y_counter += opposite
            v_x_counter -= adjacent
            print(f"adjacent:{adjacent}")
            print(f"opposite:{opposite}")
            while found_v == False:
                print("new loop")
                if map.has_wall_at(int(v_y_counter//TILESIZE), int(v_x_counter//TILESIZE) -1):
                    vertical_point = (v_x_counter, v_y_counter)
                    print(f"vp:{vertical_point}")
                    print(int(v_x_counter//TILESIZE),int(v_y_counter//TILESIZE))
                    found_v = True 
                else:
                    v_x_counter -= TILESIZE
                    if pdy == 'down':
                        v_y_counter += TILESIZE * tan
                    elif pdy == 'up':
                        v_y_counter -= TILESIZE * tan
        pygame.draw.line(screen, (255,255,255), (px,py), (v_x_counter, v_y_counter), 2)
                
            
    def cast(self, screen, px, py, pangle):
        pygame.draw.line(screen,(0,0,255),(px, py), (self.closest_point))