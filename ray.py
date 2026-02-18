from settings import *
import pygame
import math
from map import Map
from player import Player

class Ray:
    def __init__(self):
        self.wall_horizontal = None
    def detect_walls(self, screen, px, py, pangle, pdx, pdy, map):
        if math.tan(pangle) != 0:
            found_horizontal = False
            if pdy == 'up':
                o = py % TILESIZE
                a = o / (math.tan(pangle))
                hpx = px + a 
                hpy = py - o
                while found_horizontal == False:
                    if map.has_wall_at(int(hpy // TILESIZE - 1), int(hpx//TILESIZE)) == True:
                        self.wall_horizontal = (hpx, hpy)
                        found_horizontal = True
                    else:
                        if pdx == 'right':
                            hpx += a
                        if pdx == 'left':
                            hpx -= a
                        hpy -= TILESIZE

            if pdy == 'down':
                o = TILESIZE - (py % TILESIZE)
                a = o / (math.tan(pangle))
                hpx = px + a 
                hpy =  py - o
                while found_horizontal == False:
                    if map.has_wall_at(int(hpy // TILESIZE), int(hpx//TILESIZE)) == True:
                        self.wall_horizontal = (hpx, hpy)
                        found_horizontal = True
                    else:
                        if pdx == 'right':
                            hpx += a
                        if pdx == 'left':
                            hpx -= a
                        hpy += TILESIZE
            print(int(hpx//TILESIZE))
            print(o, a, hpx, hpy)
            print(self.wall_horizontal)
        



        


    def cast(self, screen, px, py, pangle):
        pygame.draw.line(screen,(0,0,255),(px, py), (px + math.cos(pangle) * 99, py - math.sin(pangle) * 99))
    