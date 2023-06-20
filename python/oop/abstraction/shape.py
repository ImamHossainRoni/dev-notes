from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Creating objects and using abstraction
circle = Circle(5)
rectangle = Rectangle(4, 6)
shapes = [circle, rectangle]

for shape in shapes:
    print("Area:", shape.calculate_area())
