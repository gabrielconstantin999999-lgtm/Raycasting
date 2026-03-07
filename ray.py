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
    def detect_walls(self, screen, player_x, player_y,player2_x, player2_y, pangle,angle, map, rnum):
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
        elif self.hd > self.vd:
            self.closest_point = vertical_point
            self.distance = self.vd
            self.v = True
        elif pangle - FOV/2 < abs(math.atan((player_y - player2_y)/(player2_x - player_x))) < pangle + FOV/2 and distance(player_x, player_y, self.closest_point[0], self.closest_point[1]) > distance(player_x, player_y, player2_x, player2_y):
            self.closest_point = player2_x, player2_y
            enemy_w = SCREEN_W / NUM_RAYS
            enemy_h = SCREEN_H / distance(player_x, player_y, player2_x, player2_y) * 18
            enemy_image = pygame.transform.scale(pygame.image.load(r"C:\Users\gabri\Documents\VSCode\Raycasting\raycastplayer.png"), (enemy_w, enemy_h))
            screen.blit(enemy_image, [rnum * (SCREEN_W/NUM_RAYS) - enemy_w/2, SCREEN_H/2 - enemy_h/2]) 
        print("1",pangle - FOV/2)
        print(abs(math.atan((player_y - player2_y)/(player2_x - player_x))) )
        print(pangle + FOV/2)
        print(pangle - FOV/2 < abs(math.atan((player_y - player2_y)/(player_x - player2_x))) < pangle + FOV/2 )
    
    def detect_player(self, screen, player, player2):
        dx = player2.x - player.x
        dy = player2.y - player.y
        ex = math.cos(player.rotation_angle) * dx + math.sin(player.rotation_angle) * dy
        ey = -math.sin(player.rotation_angle) * dx + math.cos(player.rotation_angle) * dy
        if ex <= 0:
            pass
        screen_x = SCREEN_W/2 + ey/ex * (SCREEN_W / (2 * math.tan(FOV/2)))
        start_x = screen_x - SCREEN_W/2
        end_x = screen_x + SCREEN_W/2
        player_height = SCREEN_H / abs(ex) * TILESIZE
        player_width = SCREEN_W / NUM_RAYS * 50
        print("ex",ex)
        print("pwandh: ", player_width, player_height)
        enemy_image = pygame.transform.scale(pygame.image.load(r"C:\Users\gabri\Documents\VSCode\Raycasting\raycastplayer.png"), (player_width, player_height))
        screen.blit(enemy_image, [start_x, SCREEN_H/2 - player_height/2]) 
        #pygame.draw.rect(screen, (255,0,0), (start_x, SCREEN_H/2 - player_height/2, 500, 500))
         
    def cast(self, screen, px, py):
        pass
        #pygame.draw.line(screen,(0,0,255),(px, py), (self.closest_point))