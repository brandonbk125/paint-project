import Wall
import WallObject
import Paint
import Room
import Shape


# get user input (int)
def get_int(user_prompt: str):
    valid = False
    while not valid:
        try:
            user_input = int(input(user_prompt))
            valid = True
            return user_input
        except ValueError:
            input_error()


# get user input (float)
def get_float(user_prompt: str):
    valid = False
    while not valid:
        try:
            user_input = float(input(user_prompt))
            valid = True
            return user_input
        except ValueError:
            input_error()


# get user input (string)
def get_str(user_prompt: str):
    return input(user_prompt)


# gets the shape of an object from the user
def get_shape(user_prompt: str):
    valid = False
    shape = None
    while not valid:
        try:
            user_input = int(input("What is the shape of the " + user_prompt + "? (1: Rectangle, 2: Circle, 3: "
                                                                               "Triangle): "))
            if user_input < 1 or user_input > 3:
                raise ValueError
            else:
                valid = True
                match user_input:
                    case 1:
                        shape = Shape.Rectangle()
                    case 2:
                        shape = Shape.Circle()
                    case 3:
                        shape = Shape.Triangle()
                return shape
        except ValueError:
            input_error()


# throws this error message when the user enters an invalid input
def input_error():
    print("Invalid Input")


def main():
    # create a program to calculate how much paint a user needs

    # define how much can be painted per litre of paint
    painted_wall_per_litre = 6.0

    # user inputs number of rooms
    num_rooms = get_int("Enter number of rooms to paint: ")
    rooms = []

    # for each room
    for i in range(num_rooms):
        # user inputs number of walls in each room
        num_walls = get_int("Number of walls in room " + str(i+1) + ": ")
        room = Room.Room(num_walls)
        rooms.append(room)

        # for each wall
        for j in range(num_walls):
            # user inputs wall dimensions
            wall_shape = get_shape("wall")
            wall_shape.set_dimensions()

            # creating the wall object
            wall = Wall.Wall(wall_shape)
            room.add_wall(wall)

            # user inputs number of wall objects
            num_wall_obj = get_int("Enter number of wall objects on wall " + str(j+1) + " (windows, doors etc.): ")

            # for each wall object
            for k in range(num_wall_obj):
                # user inputs dimensions of wall objects
                wall_object_shape = get_shape("wall object")
                wall_object_shape.set_dimensions()
                # adding wall objects to the wall
                wall_obj = WallObject.WallObject(wall_object_shape)
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

    # if there is 1 room or more to paint calculate cost
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
        print("Total Price: £" + str(round(total_cost, 2)))
    # if no rooms were entered do nothing
    else:
        print("No rooms entered!")


if __name__ == '__main__':
    main()

