from settings import *
import pygame
import math
from map import Map
from player import Player
def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
class Ray:
    def __init__(self):
        self.wall_horizontal_x = None
        self.wall_horizontal_y = None
        self.wall_vertical_x = None
        self.wall_vertical_y = None
        self.closest_distance = None
        self.closest_point = None
    def detect_walls(self, screen, px, py, pangle, pdx, pdy, map):
        print(pdy)
        tan = math.tan(pangle)
        if tan == 0:
            tan = 0.000001 
        found_horizontal = False
        if pdy == 'up':
            o = py % TILESIZE
            a = o / tan
            hpx = px + a 
            hpy = py - o
            while found_horizontal == False:
                print(f"grid coords: {int(hpx // TILESIZE - 1), int(hpy//TILESIZE)}")
                print(f"point: {hpx, hpy}")
                if map.has_wall_at(int(hpy // TILESIZE - 1), int(hpx//TILESIZE)) == True:
                    self.wall_horizontal_x = hpx
                    self.wall_horizontal_y = hpy
                    found_horizontal = True
                else:
                    hpy -= TILESIZE

        if pdy == 'down':
            o = TILESIZE - (py % TILESIZE)
            a = o / tan
            hpx = px + a 
            hpy =  py + o
            while found_horizontal == False:
                print(f"grid coords: {int(hpx // TILESIZE), int(hpy//TILESIZE)}")
                print(f"point: {hpx, hpy}")
                if map.has_wall_at(int(hpy // TILESIZE), int(hpx//TILESIZE)) == True:
                    self.wall_horizontal_x = hpx
                    self.wall_horizontal_y = hpy
                    found_horizontal = True
                else:
                    hpy += TILESIZE
        if self.wall_horizontal_x is not None:
            horizontal_distance = distance(px,self.wall_horizontal_x,py,self.wall_horizontal_y)

        if self.wall_vertical_x is not None:
            vertical_distance = distance(px,self.wall_vertical_x,py,self.wall_vertical_y)

        self.closest_distance = min(horizontal_distance, vertical_distance)


        
        if horizontal_distance < vertical_distance:
            self.closest_point = (self.wall_horizontal_x,self.wall_horizontal_y)
        else:
            self.closest_point = (self.wall_vertical_x,self.wall_vertical_y)

    
        found_vertical = False
        if pdx == 'left':
            o = px % TILESIZE
            a = o / (math.tan(pangle))
            vpx = px + o
            vpy = py - a
            while found_vertical == False:
                print(f"grid coords: {int(vpx // TILESIZE ), int(vpy//TILESIZE-1)}")
                print(f"point: {vpx, vpy}")
                if map.has_wall_at(int(vpy // TILESIZE ), int(vpx//TILESIZE -1)) == True:
                    self.wall_vertical_x = vpx
                    self.wall_vertical_y = vpy
                    found_vertical = True
                else:
                    vpx -= TILESIZE

        if pdx == 'right':
            o = TILESIZE - (px % TILESIZE)
            a = o / (math.tan(pangle))
            vpx = px + o
            vpy =  py + a
            while found_vertical == False:
                print(f"grid coords: {int(vpx // TILESIZE), int(vpy//TILESIZE)}")
                print(f"point: {vpx, vpy}")
                if map.has_wall_at(int(vpy // TILESIZE), int(vpx//TILESIZE)) == True:
                    self.wall_vertical_x = vpx
                    self.wall_vertical_y = vpy
                    found_vertical = True
                else:
                    vpx += TILESIZE
        if self.wall_horizontal_x is not None:
            horizontal_distance = distance(px,self.wall_horizontal_x,py,self.wall_horizontal_y)

        if self.wall_vertical_x is not None:
            vertical_distance = distance(px,self.wall_vertical_x,py,self.wall_vertical_y)

        self.closest_distance = min(horizontal_distance, vertical_distance)


        
        if horizontal_distance < vertical_distance:
            self.closest_point = (self.wall_horizontal_x,self.wall_horizontal_y)
        else:
            self.closest_point = (self.wall_vertical_x,self.wall_vertical_y)

        


        
            if self.wall_horizontal_x is not None:
                horizontal_distance = distance(px,self.wall_horizontal_x,py,self.wall_horizontal_y)

            if self.wall_vertical_x is not None:
                vertical_distance = distance(px,self.wall_vertical_x,py,self.wall_vertical_y)

            self.closest_distance = min(horizontal_distance, vertical_distance)


            
            if horizontal_distance < vertical_distance:
                self.closest_point = (self.wall_horizontal_x,self.wall_horizontal_y)
            else:
                self.closest_point = (self.wall_vertical_x,self.wall_vertical_y)  

        

        



        


    def cast(self, screen, px, py, pangle):
        pygame.draw.line(screen,(0,0,255),(px, py), (self.closest_point))
    