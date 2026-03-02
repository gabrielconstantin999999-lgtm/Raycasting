from settings import *
import pygame
import math
class Player:
    def __init__(self):
        self.x = 15 * TILESIZE
        self.y = 15 * TILESIZE
        self.rotation_angle = 90 * (math.pi/180)
        self.rotation = 1 * (math.pi/180)
        self.direction_y = None
        self.direction_x = None
        self.speed = 2
        self.sens = 0.1
        self.free_mouse = False
    def update(self,screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
               self.free_mouse = True
               pygame.mouse.set_visible(True)
        if self.free_mouse == False:
                pygame.mouse.set_visible(False)
                pygame.mouse.set_pos(SCREEN_W/2, SCREEN_H/2)
                
        x,y = pygame.mouse.get_rel()
        prev_x = 0
        if keys[pygame.K_w]:
                self.x += math.cos(self.rotation_angle) * self.speed
                self.y -= math.sin(self.rotation_angle) * self.speed
        if keys[pygame.K_s]:
                self.x -= math.cos(self.rotation_angle) * self.speed
                self.y += math.sin(self.rotation_angle) * self.speed
        if x >= prev_x:
                self.rotation_angle += self.rotation * (x - prev_x) * self.sens
        if x <= prev_x:
                self.rotation_angle -= self.rotation * (prev_x - x) * self.sens
        self.rotation_angle %= 2 * math.pi
        #pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 10)
        prev_x = x


