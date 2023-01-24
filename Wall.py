import WallObject
from paintwall import calc_area


class Wall:
    def __init__(self, height: float, length: float):
        self.height = height
        self.length = length
        self.area = calc_area(height, length)
        self.wall_objs = []

    def add_wall_obj(self, wall_object: WallObject):
        self.wall_objs.append(wall_object)

    def get_paint_area(self):
        total_obstruction = 0
        for obj in self.wall_objs:
            total_obstruction += obj.area

        return self.area - total_obstruction
