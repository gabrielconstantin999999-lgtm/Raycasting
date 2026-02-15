from settings import *
import pygame
import math


class Ray:
    def __init__(self):
        self.x = None
        self.y = None
    def cast(self, screen, px, py, pangle):
        pygame.draw.line(screen,(0,0,255),(px, py), (px + math.cos(pangle) * 100, py - math.sin(pangle) * 100))