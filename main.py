#! /usr/bin/env python3
# coding: utf-8

import pygame  # import only necessary modules !
# display, mixer, draw, event, image, mouse, time
from pygame.locals import * # import all pygame constants


# # import my own modules
# import game
# import display
# import load

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
        self.num_items = 0

    def collect_items(self):
        x = self.case_position['x']
        y = self.case_position['y']
        if self.maze_map[y][x] == '$':
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

pygame.init()  # init all moduls
window = pygame.display.set_mode((15 * TILE_SIZE, 15 * TILE_SIZE)) # création d'une fenêtre
#fond = pygame.image.load("background.jpg").convert() # charger une image
image_brick = pygame.image.load("brick.png").convert_alpha() # charger une image avec fond transparent
image_floor = pygame.image.load("floor.png").convert_alpha()
image_mac_gyver = pygame.image.load("mac_gyver.png").convert_alpha()
image_guardian = pygame.image.load("murdoc.png").convert_alpha()
image_brick = pygame.transform.scale2x(image_brick)
image_floor = pygame.transform.scale2x(image_floor)
#image.set_colorkey((255,255,255)) # rendre le blanc (valeur RGB : 255,255,255) de l'image transparent
#fenetre.blit(brick, (320,240)) # coller une image sur la fenêtre


display(maze_map)

continuer = True

# main loop
while continuer:
    for event in pygame.event.get():   # parcours de la liste des evenements
        if event.type == QUIT:     # evenement de type QUIT
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                mac_gyver.go("left")
            if event.key == K_RIGHT:
                mac_gyver.go("right")
            if event.key == K_UP:
                mac_gyver.go("up")
            if event.key == K_DOWN:
                mac_gyver.go("down")

            display(maze_map)

# if __name__ == "__main__":
    # do stuff
