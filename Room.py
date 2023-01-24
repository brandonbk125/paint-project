import Wall


class Room:
    def __init__(self, num_walls):
        self._walls = []

    def add_wall(self, wall: Wall):
        self._walls.append(wall)

    def get_walls(self):
        return self._walls



