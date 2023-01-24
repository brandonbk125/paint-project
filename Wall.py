import WallObject
from paintwall import calc_area


class Wall:
    def __init__(self, height: float, length: float):
        self._height = height
        self._length = length
        self._area = calc_area(height, length)
        self._wall_objs = []

    def add_wall_obj(self, wall_object: WallObject):
        self._wall_objs.append(wall_object)

    def get_paint_area(self):
        total_obstruction = 0
        for obj in self._wall_objs:
            total_obstruction += obj._area

        return self._area - total_obstruction
