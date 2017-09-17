#! /usr/bin/env python3
# coding: utf-8

import pygame  # import only necessary modules !
# display, mixer, draw, event, image, mouse, time
from pygame.locals import * # import all pygame constants


# # import my own modules
from init import *
from game import *
from display import *
from constants import *


# pygame and objects init
lvl = Lvl(maze_map)
mac_gyver = Character(lvl)

display(lvl.map, mac_gyver.pixel_position, images, window)

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
            display(lvl.map, mac_gyver.pixel_position, images, window)
        if mac_gyver.victory():
            print("You have won !")
            continuer = False





# if __name__ == "__main__":
    # do stuff
