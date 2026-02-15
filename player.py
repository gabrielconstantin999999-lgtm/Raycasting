from settings import *
import pygame
import math
class Player:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.rotation_angle = 45 * (math.pi/180)
        self.rotation = 1 * (math.pi/180)
    def update(self,screen):
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
        if self.rotation_angle >= 2 * math.pi:
              self.rotation_angle = 0
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 10)
        print(f"angle: {self.rotation_angle}")
        print(f"x: {self.x}")
        print(f"y: {self.y}")
        print(f"cosx: {math.cos(self.rotation_angle)}")
        print(f"siny: {math.sin(self.rotation_angle)}")


