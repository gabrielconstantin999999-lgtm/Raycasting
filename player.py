from settings import *
import pygame
import math
from map import Map
class Player:
    def __init__(self, x, y):
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.rotation_angle = 90 * (math.pi/180)
        self.rotation = 1 * (math.pi/180)
        self.direction_y = None
        self.direction_x = None
        self.speed = 2
        self.sens = 0.1
    def update(self,screen, map):
        free_mouse = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
               free_mouse = True
               pygame.mouse.set_visible(True)
        if free_mouse == False:
                pygame.mouse.set_visible(False)
                pygame.mouse.set_pos(SCREEN_W/2, SCREEN_H/2)
                
        x_change, y_change = pygame.mouse.get_rel()
        prev_x = 0
        if keys[pygame.K_w]:
                self.x += math.cos(self.rotation_angle) * self.speed
                self.y -= math.sin(self.rotation_angle) * self.speed
                if map.has_wall_at(int(self.y//TILESIZE), int(self.x//TILESIZE)):
                       self.x -= math.cos(self.rotation_angle) * self.speed
                       self.y += math.sin(self.rotation_angle) * self.speed
        if keys[pygame.K_s]:
                self.x -= math.cos(self.rotation_angle) * self.speed
                self.y += math.sin(self.rotation_angle) * self.speed
                if map.has_wall_at(int(self.y//TILESIZE), int(self.x//TILESIZE)):
                       self.x += math.cos(self.rotation_angle) * self.speed
                       self.y -= math.sin(self.rotation_angle) * self.speed
        '''
        if keys[pygame.K_a]:
               self.x -= math.cos(self.rotation_angle + 90 * math.pi / 180) * self.speed
               self.y += math.sin(self.rotation_angle + 90 * math.pi / 180) * self.speed
        if keys[pygame.K_d]:
               self.x += math.cos(self.rotation_angle - 90 * math.pi / 180) * self.speed
               self.y += math.sin(self.rotation_angle - 90 * math.pi / 180) * self.speed
               '''
        if x_change >= prev_x:
                self.rotation_angle += self.rotation * (x_change - prev_x) * self.sens
        if x_change <= prev_x:
                self.rotation_angle -= self.rotation * (prev_x - x_change) * self.sens
        self.rotation_angle %= 2 * math.pi
        #pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 10)
        prev_x = x_change
   
       


