import WallObject
import Paint
from paintwall import calc_area


class Wall:
    def __init__(self, height: float, length: float):
        self._paint = None
        self._height = height
        self._length = length
        self._area = calc_area(height, length)
        self._wall_objs = []
        self._coats = 0

    def add_wall_obj(self, wall_object: WallObject):
        self._wall_objs.append(wall_object)

    def get_paint_area(self):
        total_obstruction = 0
        for obj in self._wall_objs:
            total_obstruction += obj.get_area()

        return self._area - total_obstruction

    def set_coats(self, num_coats):
        self._coats = num_coats

    def get_coats(self):
        return self._coats

    def set_paint(self, paint: Paint):
        self._paint = paint

    def get_paint(self):
        return self._paint
