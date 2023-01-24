import Wall


class Room:
    def __init__(self, num_walls):
        self.walls = []

    def add_wall(self, wall: Wall):
        self.walls.append(wall)

