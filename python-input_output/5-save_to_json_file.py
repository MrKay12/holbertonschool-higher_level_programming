#!/usr/bin/python3
""" Args:
        my_obj: The Python object to save to the file.
        filename (str): The name of the file to save the object in.

    Returns:
        None"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
