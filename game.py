"""Defines main game classes"""
from random import randint
from constants import *


class Lvl:
    """Lvl class, contains maze_map and items"""
    def __init__(self, maze_map, items):
        self.maze_map = maze_map
        self.items = {}
        for item in items:
            self.items[item] = Item(self.random_position())

    def reset(self):
        """Places all items randomly in the maze_map"""
        for item in self.items:
            self.maze_map[self.items[item].pos_y][self.items[item].pos_x] = " "
            self.items[item] = Item(self.random_position())

    def free_path(self, pos_x, pos_y, direction):
        """Test if the path is free (no wall) in a given start position and direction"""
        return (direction == LEFT and pos_x > 0 and
                self.maze_map[pos_y][pos_x-1] != "#" or
                direction == RIGHT and pos_x < (MAP_LENGTH - 1) and
                self.maze_map[pos_y][pos_x+1] != "#" or
                direction == UP and pos_y > 0 and
                self.maze_map[pos_y-1][pos_x] != "#" or
                direction == DOWN and pos_y < (MAP_HEIGHT - 1) and
                self.maze_map[pos_y+1][pos_x] != "#")

    def random_position(self):
        """Randomly choses a free position in the maze_map to place an item"""
        pos_x = 0
        pos_y = 0
        while self.maze_map[pos_y][pos_x] != " ":
            pos_x = randint(0, (MAP_LENGTH - 1))
            pos_y = randint(0, (MAP_HEIGHT - 1))
        self.maze_map[pos_y][pos_x] = "*"
        return (pos_x, pos_y)


class Item:
    """Describes an item"""
    def __init__(self, position):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.show = True

    @property
    def pixel_position(self):
        """Pipos_xel position of the item, useful when bliting the image"""
        return [self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE]


class Character:
    """Describes the main character"""
    def __init__(self, lvl, items):
        self.lvl = lvl
        self.reset()
        self.item_msg = {}
        for item in items:
            self.item_msg[item] = items[item]["msg"]

    def reset(self):
        """Puts the character in his initial spot and clears his items"""
        self.pos_y, self.pos_x = self._initial_position(self.lvl)
        self.num_items = 0

    def move_to(self, direction):
        """Move the character in a given direction if possible"""
        if self.lvl.free_path(self.pos_x, self.pos_y, direction):
            if direction == LEFT:
                self.pos_x -= 1
            elif direction == RIGHT:
                self.pos_x += 1
            elif direction == UP:
                self.pos_y -= 1
            elif direction == DOWN:
                self.pos_y += 1
            else:
                print("error: unknown direction")
            self._collect_items()

    def _collect_items(self):
        """Collect items found in the way"""
        for item in self.lvl.items:
            if (self.lvl.items[item].pos_x == self.pos_x and
                    self.lvl.items[item].pos_y == self.pos_y and
                    self.lvl.items[item].show):
                self.num_items += 1
                self.lvl.items[item].show = False
                print(self.item_msg[item])

    def _initial_position(self, lvl):
        """Get initial character's position from the maze_map"""
        num_line = 0
        for line in lvl.maze_map:
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
        return [self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE]

    @property
    def status(self):
        """Character's status (WIN, LOST or ALIVE)"""
        if self.lvl.maze_map[self.pos_y][self.pos_x] == '.':
            if self.num_items == len(self.lvl.items):
                return WIN
            return LOST
        return ALIVE
