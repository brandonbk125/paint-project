import Wall


# the Room class contains information about a Room to be painted by the user
# a Room has a number of Walls
class Room:
    def __init__(self, num_walls):
        self._walls = []

    # add a Wall to the Room to be painted
    def add_wall(self, wall: Wall):
        self._walls.append(wall)

    # get the list of Walls to be painted
    def get_walls(self):
        return self._walls



