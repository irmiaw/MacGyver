"""Defines main game classes"""
from random import randint
from constants import *


class Lvl:
    """Lvl class, contains map and items"""
    def __init__(self, map, items):
        self.map = map
        self.items = {}
        for item in items:
            self.items[item] = Item(self.random_position())

    def free_path(self, x, y, direction):
        """Test if the path is free (no wall) in a given start position and direction"""
        return (direction == LEFT and x > 0 and self.map[y][x-1] != "#" or
                direction == RIGHT and x < (MAP_LENGTH - 1) and self.map[y][x+1] != "#" or
                direction == UP and y > 0 and self.map[y-1][x] != "#" or
                direction == DOWN and y < (MAP_HEIGHT - 1) and self.map[y+1][x] != "#")

    def random_position(self):
        """Randomly choses a free position in the map to place an item"""
        x = 0
        y = 0
        while self.map[y][x] != " ":
            x = randint(0, (MAP_LENGTH - 1))
            y = randint(0, (MAP_HEIGHT - 1))
        return (x, y)


class Item:
    """Describes an item"""
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.show = True

    @property
    def pixel_position(self):
        """Pixel position of the item, useful when bliting the image"""
        return [self.x * TILE_SIZE, self.y * TILE_SIZE]


class Character:
    """Describes the main character"""
    def __init__(self, lvl):
        self.y, self.x = self._initial_position(lvl)
        self.num_items = 0
        self.lvl = lvl

    def go(self, direction):
        """Move the character in a given direction if possible"""
        if self.lvl.free_path(self.x, self.y, direction):
            if direction == LEFT:
                self.x -= 1
            elif direction == RIGHT:
                self.x += 1
            elif direction == UP:
                self.y -= 1
            elif direction == DOWN:
                self.y += 1
            else:
                print("error: unknown direction")
            self._collect_items()

    def _collect_items(self):
        """Collect items found in the way"""
        for item in self.lvl.items:
            if (self.lvl.items[item].x == self.x and
                    self.lvl.items[item].y == self.y and
                    self.lvl.items[item].show):
                self.num_items += 1
                self.lvl.items[item].show = False

    def _initial_position(self, lvl):
        """Get initial character's position from the map"""
        num_line = 0
        for line in lvl.map:
            num_column = 0
            for case in line:
                if case == "@":
                    return (num_line, num_column)
                num_column += 1
            num_line += 1
        # if found nothing raise error

    @property
    def pixel_position(self):
        """Pixel position of the character, useful when bliting the image"""
        return [self.x * TILE_SIZE, self.y * TILE_SIZE]

    @property
    def status(self):
        """Character's status (WIN, LOST or ALIVE)"""
        if self.lvl.map[self.y][self.x] == '.':
            if self.num_items == len(self.lvl.items):
                return WIN
            return LOST
        return ALIVE
