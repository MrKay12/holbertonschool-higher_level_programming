#!/usr/bin/python3
"""Args:
        filename (str): The name of the file to load the JSON data from

    Returns:
        object: The Python object created from the JSON data"""

import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
