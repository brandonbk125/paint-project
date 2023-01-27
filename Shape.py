from abc import ABC, abstractmethod
import math
from paintwall import get_float


# abstract class Shape
# blueprint for all Shape classes
class Shape(ABC):
    # gets the area of a shape
    def get_area(self):
        pass

    # sets the dimensions of a shape
    def set_dimensions(self):
        pass


# Rectangle class
class Rectangle(Shape):
    def __init__(self):
        self._height = 0.0
        self._length = 0.0

    def get_area(self):
        return self._height * self._length

    def set_dimensions(self):
        self._height = get_float("Enter height of rectangle (m): ")
        self._length = get_float("Enter length of rectangle (m): ")

    # sets the height of a Rectangle
    def set_height(self, height: float):
        self._height = height

    # sets the length of a Rectangle
    def set_length(self, length: float):
        self._length = length


# Circle class
class Circle(Shape):
    def __init__(self):
        self._diameter = 0.0

    def get_area(self):
        return math.pi * math.pow(self._diameter/2, 2)

    def set_dimensions(self):
        self._diameter = get_float("Enter diameter of circle (m): ")

    # sets the Diameter of a Circle
    def set_diameter(self, diameter: float):
        self._diameter = diameter


# Triangle class
class Triangle(Shape):
    def __init__(self):
        self._base = 0.0
        self._height = 0.0

    def get_area(self):
        return 0.5 * self._base * self._height

    def set_dimensions(self):
        self._base = get_float("Enter base of triangle (m): ")
        self._height = get_float("Enter height of triangle (m): ")

    # sets the base of a Triangle
    def set_base(self, base: float):
        self._base = base

    # sets the height of a Triangle
    def set_height(self, height: float):
        self._height = height
