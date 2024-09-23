#!/usr/bin/python3
""" Write a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.
     Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance or inherited instance of a_class,
                False otherwise."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
