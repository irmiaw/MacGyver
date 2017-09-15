
from init import *


# Constants
TILE_SIZE = 40

def display(maze_map, mac_position, images):
    num_line = 0
    for line in maze_map:
        num_column = 0
        for case in line:
            x = num_column * TILE_SIZE
            y = num_line * TILE_SIZE

            if case == "#":
                window.blit(images.brick, (x,y))
            elif case == " " or case == ".":
                window.blit(images.floor, (x,y))

            if case == ".":
                window.blit(images.guardian, (x,y))
            num_column += 1
        num_line += 1

    window.blit(images.mac_gyver, mac_position)
    pygame.display.flip()
