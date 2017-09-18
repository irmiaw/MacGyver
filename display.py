

import pygame
from constants import TILE_SIZE


def draw(lvl, mac_position, images, window):
    num_line = 0
    for line in lvl.map:
        num_column = 0
        for case in line:
            x = num_column * TILE_SIZE
            y = num_line * TILE_SIZE

            if case == "#":
                window.blit(images.brick, (x,y))
            else:
                window.blit(images.floor, (x,y))

            if case == ".":
                window.blit(images.guardian, (x,y))
                
            num_column += 1
        num_line += 1

    window.blit(images.mac_gyver, mac_position)
    window.blit(images.needle, lvl.items["needle"].pixel_position)
    window.blit(images.tube, lvl.items["tube"].pixel_position)
    window.blit(images.ether, lvl.items["ether"].pixel_position)
    
    pygame.display.flip()
