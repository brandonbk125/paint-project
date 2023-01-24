import Wall
import WallObject


def calc_area(height: float, length: float):
    return height*length


def get_int(user_prompt: str):
    valid = False
    while not valid:
        try:
            user_input = int(input(user_prompt))
            valid = True
            return user_input
        except ValueError:
            input_error()


def get_float(user_prompt: str):
    valid = False
    while not valid:
        try:
            user_input = float(input(user_prompt))
            valid = True
            return user_input
        except ValueError:
            input_error()


def input_error():
    print("Invalid Input")


def get_num_wall_objs():
    valid = False
    while not valid:
        try:

            valid = True
            return num_wall_obj
        except ValueError:
            input_error()


def main():
    # create a program to paint wall, measuring tape how much something measures

    # define how much can be painted per litre of paint
    painted_wall_per_litre = 6.0

    # user inputs wall dimensions
    wall_height = get_float("Enter height of wall (m): ")
    wall_length = get_float("Enter length of wall (m): ")

    num_wall_obj = get_int("Enter number of wall objects (windows, doors etc.): ")
    # creating the wall object
    wall = Wall.Wall(wall_height, wall_length)

    for _ in range(num_wall_obj):
        object_height = get_float("Enter object height (m): ")
        object_length = get_float("Enter object length (m): ")

        wall_obj = WallObject.WallObject(object_height, object_length)
        wall.add_wall_obj(wall_obj)

        # get number of paint coats
        coats = get_int("Enter number of coats needed: ")

    paint_needed = (wall.get_paint_area() / painted_wall_per_litre) * coats
    # print(round(wall.area, 3))
    # print(round(wall.get_paint_area(), 3))

    print("Paint needed (litres): " + str(round(paint_needed, 3)))


if __name__ == '__main__':
    main()

