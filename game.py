"""Defines main game classes"""
from random import randint
from constants import *


"""Lvl class, contains map and items"""
class Lvl:
    def __init__(self, map, items):
        self.map = map
        self.items = {}
        for item in items:
            self.items[item] = Item(self.random_position())

    """Test if the path is free (no wall) in a given start position and direction"""
    def free_path(self, x, y, direction):
        return (direction == LEFT and x > 0 and self.map[y][x-1] != "#" or
        direction == RIGHT and x < (MAP_LENGTH - 1) and self.map[y][x+1] != "#" or
        direction == UP and y > 0 and self.map[y-1][x] != "#" or
        direction == DOWN and y < (MAP_HEIGHT - 1) and self.map[y+1][x] != "#")
        
    """Randomly choses a free position in the map to place an item"""
    def random_position(self):
        x = 0
        y = 0
        while self.map[y][x] != " ":
            x = randint(0, (MAP_LENGTH - 1))
            y = randint(0, (MAP_HEIGHT - 1))
        return (x, y)


"""Describes an item"""
class Item:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.show = True
    
    """Pixel position of the item, useful when bliting the image"""
    @property
    def pixel_position(self):
        return [self.x * TILE_SIZE, self.y * TILE_SIZE]


"""Describes the main character"""
class Character(Lvl):
    def __init__(self, lvl):
        self.y, self.x = self._initial_position(lvl)
        self.num_items = 0
        self.lvl = lvl

    """Move the character in a given direction if possible"""
    def go(self, direction):
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

    """Collect items found in the way"""
    def _collect_items(self):
        for item in self.lvl.items:
            if (self.lvl.items[item].x == self.x and
                    self.lvl.items[item].y == self.y and
                    self.lvl.items[item].show == True):
                self.num_items += 1
                self.lvl.items[item].show = False
    
    """Get initial character's position from the map"""
    def _initial_position(self, lvl):
        num_line = 0
        for line in lvl.map:
            num_column = 0
            for case in line:
                if case == "@":
                    return (num_line, num_column)
                num_column += 1
            num_line += 1
        # if found nothing raise error

    """Pixel position of the character, useful when bliting the image"""
    @property
    def pixel_position(self):
        return [self.x * TILE_SIZE, self.y * TILE_SIZE]

    """Character's status (WIN, LOST or ALIVE)"""
    @property
    def status(self):
        if self.lvl.map[self.y][self.x] == '.':
            if self.num_items == len(self.lvl.items):
                return WIN
            else:
                return LOST
        return ALIVE
