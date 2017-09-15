#! /usr/bin/env python3
# coding: utf-8

import pygame  # import only necessary modules !
# display, mixer, draw, event, image, mouse, time
from pygame.locals import * # import all pygame constants


# # import my own modules
# import game
# import display
# import init

# Constants
TILE_SIZE = 40

# '#': brick
# ' ': floor
# '.': guardian
maze_map = ["###############",
            "      #  #     ",
            "#  ## # ## #  #",
            "# #  ##    ####",
            "#    # # ### ##",
            "#  # # #   #   ",
            "# ## #  ##   # ",
            "# ##  #  ### # ",
            "#   #  #    #  ",
            "###  # ### ## #",
            "#  # # # #    #",
            "## # ##  ### ##",
            "#       ##   ##",
            "# # # #    #  .",
            "###############",
]

class Character():
    def __init__(self, maze_map):
        self.case_position = {'x': 2, 'y': 1}
        self.maze_map = maze_map
        self.num_items = 3  # for now Mac Gyver has all items

    def collect_items(self):
        x = self.case_position['x']
        y = self.case_position['y']
        if self.maze_map[y][x] == '$':  # replace with a item list instead of '$'
            self.maze_map[y][x] = ' '
            self.num_items += 1

    def go(self, direction):
        x = self.case_position['x']
        y = self.case_position['y']
        if direction == "left":
            if x > 0 and self.maze_map[y][x-1] != "#":
                self.case_position['x'] -= 1
        elif direction == "right":
            if x < 14 and maze_map[y][x+1] != "#":
                self.case_position['x'] += 1
        elif direction == "up":
            if y > 0 and maze_map[y-1][x] != "#":
                self.case_position['y'] -= 1
        elif direction == "down":
            if y < 14 and maze_map[y+1][x] != "#":
                self.case_position['y'] += 1
        else:
            print("error: unknown direction")
        self.collect_items()

    def victory(self):
        x = self.case_position['x']
        y = self.case_position['y']
        if self.maze_map[y][x] == '.' and self.num_items == 3:
            return True
        else:
            return False


    @property
    def pixel_position(self):
        return [self.case_position['x'] * TILE_SIZE, self.case_position['y'] * TILE_SIZE]




def display(maze_map):
    num_line = 0
    for line in maze_map:
        num_column = 0
        for case in line:
            x = num_column * TILE_SIZE
            y = num_line * TILE_SIZE

            if case == "#":
                window.blit(image_brick, (x,y))
            elif case == " " or case == ".":
                window.blit(image_floor, (x,y))

            if case == ".":
                window.blit(image_guardian, (x,y))
            num_column += 1
        num_line += 1

    window.blit(image_mac_gyver, mac_gyver.pixel_position)
    pygame.display.flip()


# pygame and objects init
mac_gyver = Character(maze_map)

pygame.init()
window = pygame.display.set_mode((15 * TILE_SIZE, 15 * TILE_SIZE))
image_brick = pygame.image.load("brick.png").convert_alpha()
image_floor = pygame.image.load("floor.png").convert_alpha()
image_mac_gyver = pygame.image.load("mac_gyver.png").convert_alpha()
image_guardian = pygame.image.load("murdoc.png").convert_alpha()
image_brick = pygame.transform.scale2x(image_brick)
image_floor = pygame.transform.scale2x(image_floor)

display(maze_map)

continuer = True

# main loop
while continuer:
    for event in pygame.event.get():   # iteration in all events
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                mac_gyver.go("left")
            elif event.key == K_RIGHT:
                mac_gyver.go("right")
            elif event.key == K_UP:
                mac_gyver.go("up")
            elif event.key == K_DOWN:
                mac_gyver.go("down")
            display(maze_map)
        if mac_gyver.victory():
            print("You have won !")
            continuer = False





# if __name__ == "__main__":
    # do stuff
