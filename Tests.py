import unittest
import Wall
import WallObject
import Room
import Paint
import Shape
import math


class MyTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        shape = Shape.Rectangle()
        shape.set_length(10.0)
        shape.set_height(10.0)
        self.assertEqual(shape.get_area(), 100)

    def test_circle_area(self):
        shape = Shape.Circle()
        shape.set_diameter(2)
        self.assertEqual(shape.get_area(), math.pi)

    def test_triangle_area(self):
        shape = Shape.Triangle()
        shape.set_base(10.0)
        shape.set_height(5.0)
        self.assertEqual(shape.get_area(), 25.0)

    def test_add_wall(self):
        room = Room.Room(1)
        shape = Shape.Rectangle()
        shape.set_height(10.0)
        shape.set_length(10.0)
        wall = Wall.Wall(shape)
        room.add_wall(wall)

        self.assertEqual(room.get_walls()[0], wall)

    def test_add_wall_obj(self):
        shape = Shape.Rectangle()
        shape.set_height(10.0)
        shape.set_length(10.0)
        wall = Wall.Wall(shape)

        shape2 = Shape.Circle()
        shape2.set_diameter(5.0)
        wall_obj = WallObject.WallObject(shape2)

        wall.add_wall_obj(wall_obj)
        self.assertEqual(wall.get_wall_obj()[0], wall_obj)

    def test_wall_paint_area(self):
        shape = Shape.Rectangle()
        shape.set_height(10.0)
        shape.set_length(10.0)
        wall = Wall.Wall(shape)

        shape2 = Shape.Rectangle()
        shape2.set_height(2.0)
        shape2.set_length(2.0)
        wall_obj = WallObject.WallObject(shape2)

        wall.add_wall_obj(wall_obj)
        self.assertEqual(wall.get_paint_area(), 96)

    def test_paint_cost(self):
        paint = Paint.Paint("Red", 4.50)

        self.assertEqual(paint.get_cost(), 4.50)

    def test_paint_colour(self):
        paint = Paint.Paint("Red", 4.50)

        self.assertEqual(paint.get_colour(), "Red")


if __name__ == '__main__':
    unittest.main()
