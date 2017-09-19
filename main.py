#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import * # import all pygame constants


# # import my own modules
import load
import game
import display
from constants import *

def main():

    # pygame and objects init
    pygame.init()
    window = pygame.display.set_mode((15 * TILE_SIZE, 15 * TILE_SIZE))

    filenames = ["brick.png", "floor.png", "mac_gyver.png", "guardian.png", "needle.png", "tube.png", "ether.png"]
    images = load.Images(filenames)

    lvl = game.Lvl(load.map("map.xsb"))
    mac_gyver = game.Character(lvl)

    display.draw(lvl, mac_gyver.pixel_position, images, window)

    continuer = True

    # main loop
    while continuer:
        for event in pygame.event.get():   # iteration in all events
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    mac_gyver.go(LEFT)
                elif event.key == K_RIGHT:
                    mac_gyver.go(RIGHT)
                elif event.key == K_UP:
                    mac_gyver.go(UP)
                elif event.key == K_DOWN:
                    mac_gyver.go(DOWN)
                    
                display.draw(lvl, mac_gyver.pixel_position, images, window)
                
            if mac_gyver.status == WIN:
                print("You have won !")
                continuer = False
            elif mac_gyver.status == LOST:
                print("You are dead !")
                continuer = False

if __name__ == "__main__":
    main()
