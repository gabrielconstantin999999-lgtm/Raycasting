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
        
    def update(self,screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                self.x += math.cos(self.rotation_angle) * self.speed
                self.y -= math.sin(self.rotation_angle) * self.speed
        if keys[pygame.K_DOWN]:
                self.x -= math.cos(self.rotation_angle) * self.speed
                self.y += math.sin(self.rotation_angle) * self.speed
        if keys[pygame.K_RIGHT]:
                self.rotation_angle += self.rotation
        if keys[pygame.K_LEFT]:
                self.rotation_angle -= self.rotation
        self.rotation_angle %= 2 * math.pi
        #pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 10)


