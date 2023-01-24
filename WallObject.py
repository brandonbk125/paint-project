from paintwall import calc_area


class WallObject:
    def __init__(self, height: float, length: float):
        self.height = height
        self.length = length
        self.area = calc_area(height, length)
