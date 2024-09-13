#!/usr/bin/python3
""" 
Define function for integer addition
"""

def add_integer(a, b=98):
    """Adds two integers.

    Raises: TypeError: If a or b is not an integer or float.
    Returns: int: The sum of a and b, after casting floats to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
