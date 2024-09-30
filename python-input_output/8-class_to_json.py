#!/usr/bin/python3

"""Returns the dictionary description of an object for JSON serialization"""


def class_to_json(obj):
    """
    Args:
        obj: The object instance to convert to a dictionary.

    Returns:
        dict: A dictionary containing all the serializable
        attributes of the object.
    """
    return obj.__dict__
