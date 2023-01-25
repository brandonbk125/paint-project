from paintwall import calc_area


# the WallObject class holds information on an object on a Wall in a Room
# a WallObject could be a window, door, socket, etc.
class WallObject:
    def __init__(self, height: float, length: float):
        self._height = height
        self._length = length
        self._area = calc_area(height, length)

    def get_area(self):
        return self._area
