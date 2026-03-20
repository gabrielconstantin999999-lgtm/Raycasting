import pygame
from settings import *
from map import Map
from player import Player
from ray import Ray
from raycaster import Raycaster
from network import Network
from button import Button

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

map = Map()
player1 = Player(22, 5)
player2 = Player(25, 7)
ray = Ray()
clock = pygame.time.Clock()
raycaster = Raycaster()
n = None

gun = pygame.image.load(r"/home/gabriel9/Raycasting/raycasting_gun.png")
gun2 = pygame.transform.scale(gun, (640, 320))

game_state = "menu"

play_button = Button(SCREEN_W/4,400, SCREEN_W/2, SCREEN_H/4, (255,188,117))
title = Button(SCREEN_W/4,100, SCREEN_W/2, SCREEN_H/4, (255,188,117))

p1_button = Button(SCREEN_W/4,100, 200, 200, (255,188,117))
p2_button = Button(SCREEN_W*3/4,100, 200, 200, (255,188,117))
def draw_utils(gun,screen, health, ammo):
    pygame.draw.line(screen, (0,0,0), (SCREEN_W/2 - 10, SCREEN_H/2), (SCREEN_W/2 + 10, SCREEN_H/2), 2)
    pygame.draw.line(screen, (0,0,0), (SCREEN_W/2, SCREEN_H/2 - 10), (SCREEN_W/2, SCREEN_H/2 + 10), 2)
    screen.blit(gun, (28 * TILESIZE, 17 * TILESIZE))
    pygame.draw.rect(screen, (0,255,0), (100, 764, health * 6, 32))
    pygame.draw.rect(screen, (41, 46, 45), (100, 664, ammo * 6, 32))



while True:
    clock.tick(60)
    screen.fill((117, 191, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if game_state == "menu":
        title.draw(screen,"BAGNITSACYAR", (255,255,255))
        play_button.draw(screen,"PLAY",(255,255,255))
        if play_button.get_clicked():
            game_state = "wait"
    if game_state == "wait":
        if n == None:
            n = Network()
        n.send(game_state)
        game_state = n.receive()
        p1_button.draw(screen,"YOU",(255,255,255))
        if game_state == "wait":
            p2_button.draw(screen,"WAITING...",(255,255,255))
        if game_state == "game":
            p2_button.draw(screen,"FOUND",(255,255,255))
    if game_state == "game":
        player1.update(map)
        n.send([player1.x, player1.y, player1.hit])
        player1.hit = False

        p2_info = n.receive()
        if p2_info != None:
            player2.x = p2_info[0][0]
            player2.y = p2_info[0][1]
            player1.health = p2_info[1]

        raycaster.cast_rays(screen, ray, player1, player2, map)
        draw_utils(gun2,screen, player1.health, player1.ammo)

    pygame.display.update()