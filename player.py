from settings import *
import pygame
import math
class Player:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.rotation_angle = 0
        self.rotation = 2 * (math.pi/180)
        self.move_step = 3
    def update(self,screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                self.x += math.cos(abs(self.rotation_angle))
                self.y += math.sin(abs(self.rotation_angle))
        if keys[pygame.K_DOWN]:
                self.x -= math.cos(abs(self.rotation_angle))
                self.y -= math.sin(abs(self.rotation_angle))
        if keys[pygame.K_RIGHT]:
                self.rotation_angle -= self.rotation
        if keys[pygame.K_LEFT]:
                self.rotation_angle += self.rotation
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), 10)
        print(self.rotation_angle)


