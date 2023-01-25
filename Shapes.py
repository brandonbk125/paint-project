from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, height: float, length: float):
        self._height = height
        self._length = length

    def get_area(self):
        return self._height * self._length


class Circle(Shape):
    def __init__(self, diameter: float):
        self._diameter = diameter

    def get_area(self):
        return math.pi * math.pow(self._diameter/2, 2)


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self._base = base
        self._height = height

    def get_area(self):
        return 0.5 * self._base * self._height
