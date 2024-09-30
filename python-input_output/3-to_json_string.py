#!/usr/bin/python3

import json

"""Args:
        my_obj: The Python object to convert to a JSON string.

    Returns:
        str: The JSON representation of the object."""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).    """
    return json.dumps(my_obj)
