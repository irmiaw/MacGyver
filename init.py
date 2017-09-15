import pygame

# Constants
TILE_SIZE = 40

class Images:
    def __init__(self, brick, floor, mac_gyver, guardian):
        self.brick = brick
        self.floor = floor
        self.mac_gyver = mac_gyver
        self.guardian = guardian

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


pygame.init()

window = pygame.display.set_mode((15 * TILE_SIZE, 15 * TILE_SIZE))
image_brick = pygame.image.load("brick.png").convert_alpha()
image_floor = pygame.image.load("floor.png").convert_alpha()
image_mac_gyver = pygame.image.load("mac_gyver.png").convert_alpha()
image_guardian = pygame.image.load("murdoc.png").convert_alpha()
image_brick = pygame.transform.scale2x(image_brick)
image_floor = pygame.transform.scale2x(image_floor)

images = Images(image_brick, image_floor, image_mac_gyver, image_guardian)
