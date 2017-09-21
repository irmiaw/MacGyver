"""Load images, map and config data from json file"""
import json
import pygame

class Images:
    """Load images from given config parameters"""
    def __init__(self, config):
        self.brick = self.load_image(config["brick"])
        self.floor = self.load_image(config["floor"])
        self.mac_gyver = self.load_image(config["mac_gyver"])
        self.guardian = self.load_image(config["guardian"])
        self.items = {}
        for item in config["items"]:
            try:
                self.items[item] = self.load_image(config["items"][item]["img"])
            except KeyError:
                print("Missing image from \"" + item + "\"")
                exit()
    @classmethod
    def load_image(cls, filename):
        """Calls pygame to load image and convert to transparent"""
        try:
            return pygame.image.load(filename).convert_alpha()
        except FileNotFoundError:
            print("Couldn't open the image \"" + filename + "\"")
            exit()


def map_from_file(filename):
    """Load map from given filename"""
    try:
        with open(filename, "r") as map_file:
            # we will need to modify the map when placing items, so we change it to a double list
            maze_map = [list(line) for line in map_file]
        return maze_map
    except FileNotFoundError:
        print("Couldn't open map file \"" + filename + "\"")
        exit()
# map structure:
# '#': brick
# ' ': floor
# '.': guardian

def config_from_file(filename):
    """Load config from given filename"""
    try:
        with open(filename) as data:
            return json.load(data)
    except FileNotFoundError:
        print("Couldn't open config file \"" + filename + "\"")
        exit()
