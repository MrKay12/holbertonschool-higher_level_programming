#!/usr/bin/python3
""" define a class BaseGeometry"""


class BaseGeometry:
    """A class BaseGeometry with 'area' method."""

    def area(self):
        """Raise an exception for unimplemented area method."""
        raise Exception("area() is not implemented")
