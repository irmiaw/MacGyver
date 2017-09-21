"""Load images, map and config data from json file"""
import json
import pygame

"""Load images from given config parameters"""
class Images:
    def __init__(self, config):
        self.brick = self.load_image(config["brick"])
        self.floor = self.load_image(config["floor"])
        self.mac_gyver = self.load_image(config["mac_gyver"])
        self.guardian = self.load_image(config["guardian"])
        self.items = {}
        for item in config["items"]:
            self.items[item] = self.load_image(config["items"][item]["img"])

    def load_image(self, filename):
        return pygame.image.load(filename).convert_alpha()


"""Load map from given filename"""
def map(filename):
    with open(filename, "r") as f:
        map = [line for line in f]
    return map
# map structure:
# '#': brick
# ' ': floor
# '.': guardian

"""Load config from given filename"""
def config(filename):
    with open(filename) as data:
        return json.load(data)
