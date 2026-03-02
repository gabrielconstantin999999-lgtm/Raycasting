from settings import *
import pygame
import math
from map import Map
from player import Player
def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
class Ray:
    def __init__(self):
        self.closest_point = None
        self.distance = None
        self.pdx = None
        self.pdy = None
        self.hd = float('inf')
        self.vd = float('inf')
        self.v = False
        self.h = False
    def detect_walls(self, screen, px, py, pangle, map):
        self.v = False
        self.h = False
        if 90 * (math.pi/180) < pangle < 270 * (math.pi/180):
              self.pdx = 'left'
        if not 90 * (math.pi/180) < pangle < 270 * (math.pi/180):
              self.pdx = 'right'
        if 0 * (math.pi/180) < pangle < 180 * (math.pi/180):
              self.pdy = 'up'
        if not 0 * (math.pi/180) < pangle < 180 * (math.pi/180):
              self.pdy = 'down'
        tan = abs(math.tan(pangle))
        if tan == 0: tan = abs(math.tan(pangle + 0.1))
        found_h = False
        found_v = False
        h_x_counter = px
        h_y_counter = py
        v_x_counter = px
        v_y_counter = py
        if self.pdy == 'up':
            opposite = py % TILESIZE
            adjacent = opposite / tan
            if self.pdx == 'right':
                h_x_counter += adjacent
            elif self.pdx == 'left':
                h_x_counter -= adjacent
            h_y_counter -= opposite
            while found_h == False:
                if map.has_wall_at(int(h_y_counter//TILESIZE) - 1, int(h_x_counter//TILESIZE)):
                    horizontal_point = (h_x_counter, h_y_counter)
                    found_h = True 
                else:
                    h_y_counter -= TILESIZE
                    if self.pdx == 'right':
                        h_x_counter += TILESIZE/tan
                    elif self.pdx == 'left':
                        h_x_counter -= TILESIZE/tan
        if self.pdy == 'down':
            opposite = TILESIZE - (py % TILESIZE)
            adjacent = opposite / tan
            if self.pdx == 'right':
                h_x_counter += adjacent
            elif self.pdx == 'left':
                h_x_counter -= adjacent
            h_y_counter += opposite
            while found_h == False:
                if map.has_wall_at(int(h_y_counter//TILESIZE), int(h_x_counter//TILESIZE)):
                    horizontal_point = (h_x_counter, h_y_counter)
                    found_h = True 
                else:
                    h_y_counter += TILESIZE
                    if self.pdx == 'right':
                        h_x_counter += TILESIZE/tan
                    elif self.pdx == 'left':
                        h_x_counter -= TILESIZE/tan
        
        if self.pdx == 'right':
            adjacent = TILESIZE - (px % TILESIZE)
            opposite = adjacent * tan
            
            if self.pdy == 'up':
                v_y_counter -= opposite
            elif self.pdy == 'down':
                v_y_counter += opposite
            v_x_counter += adjacent
            while found_v == False:
                if map.has_wall_at(int(v_y_counter//TILESIZE), int(v_x_counter//TILESIZE)):
                    vertical_point = (v_x_counter, v_y_counter)
                    found_v = True 
                else:
                    v_x_counter += TILESIZE
                    if self.pdy == 'down':
                        v_y_counter += TILESIZE * tan
                    elif self.pdy == 'up':
                        v_y_counter -= TILESIZE * tan
        if self.pdx == 'left':
            adjacent = px % TILESIZE
            opposite = adjacent * tan
            
            if self.pdy == 'up':
                v_y_counter -= opposite
            elif self.pdy == 'down':
                v_y_counter += opposite
            v_x_counter -= adjacent
            while found_v == False:
                if map.has_wall_at(int(v_y_counter//TILESIZE), int(v_x_counter//TILESIZE) -1):
                    vertical_point = (v_x_counter, v_y_counter)
                    found_v = True 
                else:
                    v_x_counter -= TILESIZE
                    if self.pdy == 'down':
                        v_y_counter += TILESIZE * tan
                    elif self.pdy == 'up':
                        v_y_counter -= TILESIZE * tan
                
        
        if found_h:
            self.hd = distance(px, h_x_counter, py, h_y_counter)
        if found_v:
            self.vd = distance(px, v_x_counter, py, v_y_counter)

        if self.hd < self.vd:
            self.closest_point = horizontal_point
            self.distance = self.hd
            self.h = True
        else:
            self.closest_point = vertical_point
            self.distance = self.vd
            self.v = True
    def cast(self, screen, px, py):
        pass
        #pygame.draw.line(screen,(0,0,255),(px, py), (self.closest_point))