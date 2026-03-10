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
        self.image = pygame.image.load(r"C:\Users\gabri\Documents\VSCode\Raycasting\raycastplayer.png")
    def detect_walls(self,player,angle, map, rnum):
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
        h_x_counter = player.x
        h_y_counter = player.y
        if self.direction_y == 'up':
            opposite = player.y % TILESIZE
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
                elif map.has_player_at(int(h_y_counter//TILESIZE) - 1, int(h_x_counter//TILESIZE)):
                    player.draw(screen, distance(player.x, player.y, h_x_counter, h_y_counter), player, player2, rnum)
                else:
                    h_y_counter -= TILESIZE
                    if self.direction_x == 'right':
                        h_x_counter += TILESIZE/tan
                    elif self.direction_x == 'left':
                        h_x_counter -= TILESIZE/tan
        if self.direction_y == 'down':
            opposite = TILESIZE - (player.y % TILESIZE)
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
                elif map.has_player_at(int(h_y_counter//TILESIZE), int(h_x_counter//TILESIZE)):
                    player.draw(screen, distance(player.x, player.y, h_x_counter, h_y_counter), player, player2, rnum)
                else:
                    h_y_counter += TILESIZE
                    if self.direction_x == 'right':
                        h_x_counter += TILESIZE/tan
                    elif self.direction_x == 'left':
                        h_x_counter -= TILESIZE/tan

        #Vertical checking
        found_v = False
        self.v = False
        v_x_counter = player.x
        v_y_counter = player.y
        if self.direction_x == 'right':
            adjacent = TILESIZE - (player.x % TILESIZE)
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
                elif map.has_player_at(int(v_y_counter//TILESIZE), int(v_x_counter//TILESIZE)):
                    player.draw(screen, distance(player.x, player.y, v_x_counter, v_y_counter), player, player2, rnum)
                else:
                    v_x_counter += TILESIZE
                    if self.direction_y == 'down':
                        v_y_counter += TILESIZE * tan
                    elif self.direction_y == 'up':
                        v_y_counter -= TILESIZE * tan
        if self.direction_x == 'left':
            adjacent = player.x % TILESIZE
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
                elif map.has_player_at(int(v_y_counter//TILESIZE), int(v_x_counter//TILESIZE) -1):
                    player.draw(screen, distance(player.x, player.y, v_x_counter, v_y_counter), player, player2, rnum)
                else:
                    v_x_counter -= TILESIZE
                    if self.direction_y == 'down':
                        v_y_counter += TILESIZE * tan
                    elif self.direction_y == 'up':
                        v_y_counter -= TILESIZE * tan
        #Closest point
        if found_h:
            self.hd = distance(player.x, h_x_counter, player.y, h_y_counter)
        if found_v:
            self.vd = distance(player.x, v_x_counter, player.y, v_y_counter)

        if self.hd < self.vd:
            self.closest_point = horizontal_point
            self.distance = self.hd
            self.h = True
        elif self.hd > self.vd:
            self.closest_point = vertical_point
            self.distance = self.vd
            self.v = True
    
    def detect_player(self, screen, player, player2, wall_distances):
        dx = player2.x - player.x
        dy = player2.y - player.y
        world_angle = math.atan2(-dy, dx) % (2 * math.pi)
        relative_angle = (world_angle - player.rotation_angle + math.pi) % (2 * math.pi) - math.pi
        
        if abs(relative_angle) > FOV / 2:
            return
        
        dist = math.sqrt(dx**2 + dy**2)
        if dist < 10:
            return
        
        screen_x = SCREEN_W/2 + (relative_angle / (FOV/2)) * (SCREEN_W/2)
        height = int(min(SCREEN_H * 3, SCREEN_H / dist * TILESIZE))
        width = height
        col_start = int(screen_x - width/2)
        top_y = SCREEN_H//2 - height//2

        # CACHING:
        # pygame.transform.scale is slow — it redraws every pixel of the image
        # at the new size. If we call it every frame, that's 60 rescales per second.
        # Instead we save the last scaled result and only redo it when the size changes.
        # Size changes when dist changes i.e. player2 moves closer or further.
        # If player2 is standing still, we reuse the same surface every frame for free.
        if not hasattr(self, '_cached_size') or self._cached_size != (width, height):
            # size is different from last frame — rescale and save it
            self._cached_enemy = pygame.transform.scale(self.image, (width, height))
            self._cached_size = (width, height)
        # size is same as last frame — skip the rescale, use saved surface
        enemy = self._cached_enemy

        line_width = SCREEN_W / NUM_RAYS
        for col in range(col_start, col_start + width):
            wall_idx = int(col / line_width)
            if 0 <= wall_idx < len(wall_distances):
                if dist < wall_distances[wall_idx]:
                    screen.blit(enemy, (col, top_y),area=pygame.Rect(col - col_start, 0, 1, height))
    def cast(self, screen, px, py):
        pass
        #pygame.draw.line(screen,(0,0,255),(px, py), (self.closest_point))