import unittest
import Wall
import WallObject
import Room
import Paint
import paintwall


class MyTestCase(unittest.TestCase):
    def test_calc_area(self):
        self.assertEqual(paintwall.calc_area(10, 10), 100)

    def test_add_wall(self):
        room = Room.Room(1)
        wall = Wall.Wall(10, 10)
        room.add_wall(wall)

        self.assertEqual(room.get_walls()[0], wall)

    def test_add_wall_obj(self):
        wall = Wall.Wall(10, 10)
        wall_obj = WallObject.WallObject(2, 2)

        wall.add_wall_obj(wall_obj)
        self.assertEqual(wall.get_wall_obj()[0], wall_obj)

    def test_wall_paint_area(self):
        wall = Wall.Wall(10, 10)
        wall_obj = WallObject.WallObject(2, 2)

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
