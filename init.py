import pygame

from constants import TILE_SIZE


class Images:
    def __init__(self, filenames):
        self.brick = pygame.transform.scale2x(self.load_image(filenames[0]))
        self.floor = pygame.transform.scale2x(self.load_image(filenames[1]))
        self.mac_gyver = self.load_image(filenames[2])
        self.guardian = self.load_image(filenames[3])

    def load_image(self, filename):
        return pygame.image.load(filename).convert_alpha()

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

filenames = ["brick.png", "floor.png", "mac_gyver.png", "murdoc.png"]
images = Images(filenames)
