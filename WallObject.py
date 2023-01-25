import Shape


# the WallObject class holds information on an object on a Wall in a Room
# a WallObject could be a window, door, socket, etc.
class WallObject:
    def __init__(self, shape: Shape):
        self._area = shape.get_area()

    def get_area(self):
        return self._area
