#! /usr/bin/env python3
# coding: utf-8
"""Main game file"""

import pygame
from pygame.locals import * # import all pygame constants

import load
import game
import display
from constants import *

def main():
    """Main function"""
    pygame.init()
    window = pygame.display.set_mode((MAP_LENGTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

    config = load.config_from_file("config.json")
    images = load.Images(config)
    lvl = game.Lvl(load.map_from_file("map.xsb"), config["items"])
    mac_gyver = game.Character(lvl, config["items"])

    display.draw(lvl, mac_gyver, images, window)

    continue_game = True
    end_game = False

    # Main game loop
    print(config["start_msg"])
    while continue_game:
        for event in pygame.event.get():   # iteration in all events
            if event.type == QUIT:
                continue_game = False
            if event.type == KEYDOWN:
                if not end_game:
                    if event.key == K_LEFT:
                        mac_gyver.move_to(LEFT)
                    elif event.key == K_RIGHT:
                        mac_gyver.move_to(RIGHT)
                    elif event.key == K_UP:
                        mac_gyver.move_to(UP)
                    elif event.key == K_DOWN:
                        mac_gyver.move_to(DOWN)

                    if mac_gyver.status == WIN:
                        print(config["end_msg_win"])
                    elif mac_gyver.status == LOST:
                        print(config["end_msg_lost"])

                    if mac_gyver.status != ALIVE:
                        print("\nDo you want to replay (y/n) ?")
                        end_game = True
                else:
                    if event.key == K_y:
                        print("Ejoy!")
                        mac_gyver.reset()
                        lvl.reset()
                        end_game = False
                    elif event.key == K_n:
                        continue_game = False

                display.draw(lvl, mac_gyver, images, window)

if __name__ == "__main__":
    main()
