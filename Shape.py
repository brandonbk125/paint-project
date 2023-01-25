from abc import ABC, abstractmethod
import math
import paintwall


class Shape(ABC):
    def get_area(self):
        pass

    def set_dimensions(self):
        pass


class Rectangle(Shape):
    def __init__(self):
        self._height = 0.0
        self._length = 0.0

    def get_area(self):
        return self._height * self._length

    def set_dimensions(self):
        self._height = paintwall.get_float("Enter height of rectangle (m): ")
        self._length = paintwall.get_float("Enter length of rectangle (m): ")

    def set_height(self, height: float):
        self._height = height

    def set_length(self, length: float):
        self._length = length


class Circle(Shape):
    def __init__(self):
        self._diameter = 0.0

    def get_area(self):
        return math.pi * math.pow(self._diameter/2, 2)

    def set_dimensions(self):
        self._diameter = paintwall.get_float("Enter diameter of circle (m): ")

    def set_diameter(self, diameter: float):
        self._diameter = diameter


class Triangle(Shape):
    def __init__(self):
        self._base = 0.0
        self._height = 0.0

    def get_area(self):
        return 0.5 * self._base * self._height

    def set_dimensions(self):
        self._base = paintwall.get_float("Enter base of triangle (m): ")
        self._height = paintwall.get_float("Enter height of triangle (m): ")

    def set_base(self, base: float):
        self._base = base

    def set_height(self, height: float):
        self._height = height
