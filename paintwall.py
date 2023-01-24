def calc_area(height: float, length: float):
    return height*length


class WallObject:
    def __init__(self, height: float, length: float):
        self.height = height
        self.length = length
        self.area = calc_area(height, length)


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


class Room:
    def __init__(self, num_walls):
        self.walls = []

    def add_wall(self, wall: Wall):
        self.walls.append(wall)


class Paint:
    def __init__(self, colour : str, cost_per_litre: float):
        self.colour = colour
        self.cost_per_litre = cost_per_litre


def main():
    # create a program to paint wall, measuring tape how much something measures

    # define how much can be painted per litre of paint
    painted_wall_per_litre = 6.0

    # user inputs wall dimensions
    wall_height = float(input("Enter wall height (m): "))
    wall_length = float(input("Enter wall length (m): "))
    num_wall_obj = int(input("Enter number of wall objects (windows, doors etc.): "))

    # creating the wall object
    wall = Wall(wall_height, wall_length)

    for _ in range(num_wall_obj):
        object_height = float(input("Enter object height (m): "))
        object_length = float(input("Enter object length (m): "))
        wallobj = WallObject(object_height, object_length)
        wall.add_wall_obj(wallobj)

    coats = int(input("Enter number of coats needed: "))

    paint_needed = (wall.area / painted_wall_per_litre) * coats
    # print(round(wall.area, 3))
    print("Paint needed (litres): " + str(round(paint_needed, 3)))


if __name__ == '__main__':
    main()

