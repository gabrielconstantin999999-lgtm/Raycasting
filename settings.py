import math

TILESIZE = 32

SCREEN_W = TILESIZE * 48
SCREEN_H = TILESIZE * 27

RES = 4

NUM_RAYS = SCREEN_W / RES

FOV = 60 * (math.pi/180)


def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
