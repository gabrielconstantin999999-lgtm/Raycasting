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
        self.direction_x = None
        self.direction_y = None
        self.hd = float('inf')
        self.vd = float('inf')
    def detect_walls(self, player_x, player_y, angle, map):
        if 90 * (math.pi/180) < angle < 270 * (math.pi/180):
              self.direction_x = 'left'
        if not 90 * (math.pi/180) < angle < 270 * (math.pi/180):
              self.direction_x = 'right'
        if 0 * (math.pi/180) < angle < 180 * (math.pi/180):
              self.direction_y = 'up'
        if not 0 * (math.pi/180) < angle < 180 * (math.pi/180):
              self.direction_y = 'down'
        tan = abs(math.tan(angle))
        if tan == 0: tan = abs(math.tan(angle + 0.1))

        #Horizontal checking
        found_h = False
        self.h = False
        h_x_counter = player_x
        h_y_counter = player_y
        if self.direction_y == 'up':
            opposite = player_y % TILESIZE
            adjacent = opposite / tan
            if self.direction_x == 'right':
                h_x_counter += adjacent
            elif self.direction_x == 'left':
                h_x_counter -= adjacent
            h_y_counter -= opposite
            while found_h == False:
                if map.has_wall_at(int(h_y_counter//TILESIZE) - 1, int(h_x_counter//TILESIZE)):
                    horizontal_point = (h_x_counter, h_y_counter)
                    found_h = True 
                else:
                    h_y_counter -= TILESIZE
                    if self.direction_x == 'right':
                        h_x_counter += TILESIZE/tan
                    elif self.direction_x == 'left':
                        h_x_counter -= TILESIZE/tan
        if self.direction_y == 'down':
            opposite = TILESIZE - (player_y % TILESIZE)
            adjacent = opposite / tan
            if self.direction_x == 'right':
                h_x_counter += adjacent
            elif self.direction_x == 'left':
                h_x_counter -= adjacent
            h_y_counter += opposite
            while found_h == False:
                if map.has_wall_at(int(h_y_counter//TILESIZE), int(h_x_counter//TILESIZE)):
                    horizontal_point = (h_x_counter, h_y_counter)
                    found_h = True 
                else:
                    h_y_counter += TILESIZE
                    if self.direction_x == 'right':
                        h_x_counter += TILESIZE/tan
                    elif self.direction_x == 'left':
                        h_x_counter -= TILESIZE/tan

        #Vertical checking
        found_v = False
        self.v = False
        v_x_counter = player_x
        v_y_counter = player_y
        if self.direction_x == 'right':
            adjacent = TILESIZE - (player_x % TILESIZE)
            opposite = adjacent * tan
            
            if self.direction_y == 'up':
                v_y_counter -= opposite
            elif self.direction_y == 'down':
                v_y_counter += opposite
            v_x_counter += adjacent
            while found_v == False:
                if map.has_wall_at(int(v_y_counter//TILESIZE), int(v_x_counter//TILESIZE)):
                    vertical_point = (v_x_counter, v_y_counter)
                    found_v = True 
                else:
                    v_x_counter += TILESIZE
                    if self.direction_y == 'down':
                        v_y_counter += TILESIZE * tan
                    elif self.direction_y == 'up':
                        v_y_counter -= TILESIZE * tan
        if self.direction_x == 'left':
            adjacent = player_x % TILESIZE
            opposite = adjacent * tan
            
            if self.direction_y == 'up':
                v_y_counter -= opposite
            elif self.direction_y == 'down':
                v_y_counter += opposite
            v_x_counter -= adjacent
            while found_v == False:
                if map.has_wall_at(int(v_y_counter//TILESIZE), int(v_x_counter//TILESIZE) -1):
                    vertical_point = (v_x_counter, v_y_counter)
                    found_v = True 
                else:
                    v_x_counter -= TILESIZE
                    if self.direction_y == 'down':
                        v_y_counter += TILESIZE * tan
                    elif self.direction_y == 'up':
                        v_y_counter -= TILESIZE * tan
                
        #Closest point
        if found_h:
            self.hd = distance(player_x, h_x_counter, player_y, h_y_counter)
        if found_v:
            self.vd = distance(player_x, v_x_counter, player_y, v_y_counter)

        if self.hd < self.vd:
            self.closest_point = horizontal_point
            self.distance = self.hd
            self.h = True
        else:
            self.closest_point = vertical_point
            self.distance = self.vd
            self.v = True
    def detect_player(self, screen, player, player2):
        print(self.closest_point[0], player.x, player2.x, self.closest_point[1],player.y, player2.y)
        if (math.atan(self.closest_point[1] - player.y/self.closest_point[0] - player.x)) * math.pi/180 == player2.rotation_angle:
            pygame.draw.rect(screen, (255,0,0), (400, 400, 100, 100))
    def cast(self, screen, px, py):
        pass
        #pygame.draw.line(screen,(0,0,255),(px, py), (self.closest_point))