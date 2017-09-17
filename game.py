

from constants import *


class Lvl:
    def __init__(self, map):
        self.map = map
        # self.objects

    def free_path(self, x, y, direction):
        return (direction == LEFT and x > 0 and self.map[y][x-1] != "#" or
        direction == RIGHT and x < 14 and self.map[y][x+1] != "#" or
        direction == UP and y > 0 and self.map[y-1][x] != "#" or
        direction == DOWN and y < 14 and self.map[y+1][x] != "#")


class Character(Lvl):
    def __init__(self, lvl):
        self.x = 2 # todo: load mac position from file
        self.y = 1
        self.num_items = 3  # for now Mac Gyver has all items
        self.lvl = lvl

    def collect_items(self):
        if self.lvl.map[self.y][self.x] == '$':  # replace with a item list instead of '$'
            self.lvl.map[self.y][self.x] = ' '
            self.num_items += 1

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
            self.collect_items()

    def victory(self):
        return self.lvl.map[self.y][self.x] == '.' and self.num_items == 3

    @property
    def pixel_position(self):
        return [self.x * TILE_SIZE, self.y * TILE_SIZE]
