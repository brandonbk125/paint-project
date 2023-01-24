import Wall
import WallObject
import Paint
import Room


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


def get_str(user_prompt: str):
    return input(user_prompt)


def input_error():
    print("Invalid Input")


def main():

    # create a program to paint wall, measuring tape how much something measures

    # define how much can be painted per litre of paint
    painted_wall_per_litre = 6.0
    # user inputs number of rooms
    num_rooms = get_int("Enter number of rooms to paint: ")
    rooms = []
    # user inputs number of walls
    for i in range(num_rooms):
        # user inputs wall dimensions
        num_walls = get_int("Number of walls in room " + str(i+1) + ": ")
        room = Room.Room(num_walls)
        rooms.append(room)
        for j in range(num_walls):
            wall_height = get_float("Enter height of wall " + str(j+1) + " (m): ")
            wall_length = get_float("Enter length of wall " + str(j+1) + " (m): ")

            # creating the wall object
            wall = Wall.Wall(wall_height, wall_length)
            room.add_wall(wall)

            # user inputs number of wall objects
            num_wall_obj = get_int("Enter number of wall objects on wall " + str(j+1) + " (windows, doors etc.): ")

            for k in range(num_wall_obj):
                # user inputs dimensions of wall objects
                object_height = get_float("Enter object " + str(k+1) + " height (m): ")
                object_length = get_float("Enter object " + str(k+1) + " length (m): ")

                # adding wall objects to the wall
                wall_obj = WallObject.WallObject(object_height, object_length)
                wall.add_wall_obj(wall_obj)

            # get paint
            paint_colour = get_str("Enter paint colour for wall " + str(j+1) + ": ")

            # get paint cost
            paint_cost = get_float("Enter cost of paint per litre: ")
            paint = Paint.Paint(paint_colour, paint_cost)

            # set the paint to the wall
            wall.set_paint(paint)

            # get number of paint coats
            coats = get_int("Enter number of coats needed: ")
            wall.set_coats(coats)

    if num_rooms > 0:
        total_cost = 0
        total_paint = 0

        # calc how much paint and how much it will cost
        for room in rooms:
            for wall in room.get_walls():
                paint_needed = (wall.get_paint_area() / painted_wall_per_litre) * wall.get_coats()
                total_paint += paint_needed
                print(str(round(paint_needed, 3)) + " litres of " + wall.get_paint().get_colour() + " paint.")
                paint_cost = paint_needed * wall.get_paint().get_cost()
                total_cost += paint_cost

        print("Total Paint needed (litres): " + str(round(total_paint, 3)))
        print("Total Price: £" + str(round(total_cost,2)))
    else:
        pass


if __name__ == '__main__':
    main()

