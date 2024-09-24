from abc import ABC, abstractmethod
import math
"""
Module defining an abstract `Shape` class and its concrete implementations
`Circle` and `Rectangle`. Includes a function to display area and perimeter.
"""


class Shape(ABC):
    """
    Abstract base class for shapes. It defines two abstract methods:
    - area: to calculate the area of the shape.
    - perimeter: to calculate the perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    A concrete implementation of a Circle,
    inheriting from the Shape class.

    Attributes:
    - radius: the radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.

        Args:
        radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
        float: Area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.

        Returns:
        float: Perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A concrete implementation of a Rectangle, inheriting from the Shape class.

    Attributes:
    - width: the width of the rectangle.
    - height: the height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given width and height.

        Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        float: Area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
        float: Perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a given shape.

    Args:
    shape (Shape): An instance of a class that inherits from the Shape class.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
