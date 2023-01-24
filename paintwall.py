import Wall
import WallObject


def calc_area(height: float, length: float):
    return height*length


def get_int(user_prompt: str):
    return int(input(user_prompt))


def get_float(user_prompt: str):
    return float(input(user_prompt))


def input_error():
    print("Invalid Input")


def main():
    # create a program to paint wall, measuring tape how much something measures

    # define how much can be painted per litre of paint
    painted_wall_per_litre = 6.0

    # user inputs wall dimensions
    valid = False
    while not valid:
        try:
            wall_height = get_float("Enter wall height (m): ")
            valid = True
        except ValueError:
            input_error()

    valid = False
    while not valid:
        try:
            wall_length = get_float("Enter wall length (m): ")
            valid = True
        except ValueError:
            input_error()

    valid = False
    while not valid:
        try:
            num_wall_obj = get_int("Enter number of wall objects (windows, doors etc.): ")
            valid = True
        except ValueError:
            input_error()

    # creating the wall object
    wall = Wall.Wall(wall_height, wall_length)

    for _ in range(num_wall_obj):
        valid = False
        while not valid:
            try:
                object_height = get_float("Enter object height (m): ")
                valid = True
            except ValueError:
                input_error()

        valid = False
        while not valid:
            try:
                object_length = get_float("Enter object length (m): ")
                valid = True
            except ValueError:
                input_error()
        wall_obj = WallObject.WallObject(object_height, object_length)
        wall.add_wall_obj(wall_obj)

    valid = False
    while not valid:
        try:
            coats = get_int("Enter number of coats needed: ")
            valid = True
        except ValueError:
            input_error()

    paint_needed = (wall.get_paint_area() / painted_wall_per_litre) * coats
    # print(round(wall.area, 3))
    # print(round(wall.get_paint_area(), 3))

    print("Paint needed (litres): " + str(round(paint_needed, 3)))


if __name__ == '__main__':
    main()

