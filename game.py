

from constants import *


class Lvl:
    def __init__(self, map):
        self.map = map
        self.items = {"needle": Item(2, 1), "tube": Item(3, 1), "ether": Item(4, 1)}

    def free_path(self, x, y, direction):
        return (direction == LEFT and x > 0 and self.map[y][x-1] != "#" or
        direction == RIGHT and x < 14 and self.map[y][x+1] != "#" or
        direction == UP and y > 0 and self.map[y-1][x] != "#" or
        direction == DOWN and y < 14 and self.map[y+1][x] != "#")


class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.show = True
        
    @property
    def pixel_position(self):
        return [self.x * TILE_SIZE, self.y * TILE_SIZE]


class Character(Lvl):
    def __init__(self, lvl):
        self.y, self.x = self._initial_position(lvl)
        self.num_items = 0
        self.lvl = lvl

    def _collect_items(self):
        for item in self.lvl.items:
            if self.lvl.items[item].x == self.x and self.lvl.items[item].y == self.y:
                self.num_items += 1
                self.lvl.items[item].show = False

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

    def victory(self):
        return self.lvl.map[self.y][self.x] == '.' and self.num_items == 3
        
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
        

    @property
    def pixel_position(self):
        return [self.x * TILE_SIZE, self.y * TILE_SIZE]
