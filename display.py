"""Display management"""
import pygame
from constants import *


def draw(lvl, mac_gyver, images, window):
    """Draws the graphics of the game"""
    num_line = 0
    for line in lvl.maze_map:
        num_column = 0
        for case in line:
            img_pos = [num_column * TILE_SIZE, num_line * TILE_SIZE]

            if case == "#":
                window.blit(images.brick, img_pos)
            else:
                window.blit(images.floor, img_pos)

            if case == "." and mac_gyver.status != WIN:
                window.blit(images.guardian, img_pos)

            num_column += 1
        num_line += 1
    if mac_gyver.status != LOST:
        window.blit(images.mac_gyver, mac_gyver.pixel_position)

    for item in lvl.items:
        if lvl.items[item].show:
            window.blit(images.items[item], lvl.items[item].pixel_position)

    pygame.display.flip()
