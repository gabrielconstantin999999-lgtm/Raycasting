from settings import *
import pygame
import math
class Player:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.rotation_angle = 0 * (math.pi/180)
        self.rotation = 1 * (math.pi/180)
        self.direction_y = None
        self.direction_x = None
        
        
    def update(self,screen):
        if 90 * (math.pi/180) < self.rotation_angle < 270 * (math.pi/180):
              self.direction_x = 'left'
        if not 90 * (math.pi/180) < self.rotation_angle < 270 * (math.pi/180):
              self.direction_x = 'right'
        if 0 * (math.pi/180) < self.rotation_angle < 180 * (math.pi/180):
              self.direction_y = 'up'
        if not 0 * (math.pi/180) < self.rotation_angle < 180 * (math.pi/180):
              self.direction_y = 'down'

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                self.x += math.cos(self.rotation_angle)
                self.y -= math.sin(self.rotation_angle)
        if keys[pygame.K_DOWN]:
                self.x -= math.cos(self.rotation_angle)
                self.y += math.sin(self.rotation_angle)
        if keys[pygame.K_RIGHT]:
                self.rotation_angle -= self.rotation
        if keys[pygame.K_LEFT]:
                self.rotation_angle += self.rotation
        if abs(self.rotation_angle) >= 2 * math.pi:
              self.rotation_angle = 0
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 10)
        print(f"angle: {self.rotation_angle}")
        print(f"x: {self.x}")
        print(f"y: {self.y}")


