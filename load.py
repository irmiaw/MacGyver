"""Load images and map"""
import pygame

class Images:
    """Load images from given filname"""
    def __init__(self, filenames):
        self.brick = self.load_image(filenames[0])
        self.floor = self.load_image(filenames[1])
        self.mac_gyver = self.load_image(filenames[2])
        self.guardian = self.load_image(filenames[3])
        self.needle = self.load_image(filenames[4])
        self.tube = self.load_image(filenames[5])
        self.ether = self.load_image(filenames[6])

    def load_image(self, filename):
        return pygame.image.load(filename).convert_alpha()

def map(filename):
    """Load map from given filename"""
    with open(filename, "r") as f:
        map = [line for line in f]
    return map

# map structure:
# '#': brick
# ' ': floor
# '.': guardian

