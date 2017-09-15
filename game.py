


# Constants
TILE_SIZE = 40

class Character():
    def __init__(self, maze_map):
        self.case_position = {'x': 2, 'y': 1}
        self.maze_map = maze_map
        self.num_items = 3  # for now Mac Gyver has all items

    def collect_items(self):
        x = self.case_position['x']
        y = self.case_position['y']
        if self.maze_map[y][x] == '$':  # replace with a item list instead of '$'
            self.maze_map[y][x] = ' '
            self.num_items += 1

    def go(self, direction):
        x = self.case_position['x']
        y = self.case_position['y']
        if direction == "left":
            if x > 0 and self.maze_map[y][x-1] != "#":
                self.case_position['x'] -= 1
        elif direction == "right":
            if x < 14 and maze_map[y][x+1] != "#":
                self.case_position['x'] += 1
        elif direction == "up":
            if y > 0 and maze_map[y-1][x] != "#":
                self.case_position['y'] -= 1
        elif direction == "down":
            if y < 14 and maze_map[y+1][x] != "#":
                self.case_position['y'] += 1
        else:
            print("error: unknown direction")
        self.collect_items()

    def victory(self):
        x = self.case_position['x']
        y = self.case_position['y']
        if self.maze_map[y][x] == '.' and self.num_items == 3:
            return True
        else:
            return False


    @property
    def pixel_position(self):
        return [self.case_position['x'] * TILE_SIZE, self.case_position['y'] * TILE_SIZE]
