#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.
    Parameters:
    a (int, float): The first number to add.
    b (int, float, optional): The second number to add. Defaults to 98.
    Raises:
    TypeError: If a or b is not an integer or float.
    Returns:
    int: The sum of a and b, after casting floats to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)