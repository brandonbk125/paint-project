from paintwall import calc_area


class WallObject:
    def __init__(self, height: float, length: float):
        self._height = height
        self._length = length
        self._area = calc_area(height, length)

    def get_area(self):
        return self._area
