import pygame

class Images:
    def __init__(self, filenames):
        self.brick = self.load_image(filenames[0])
        self.floor = self.load_image(filenames[1])
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
