#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list and saves
the list to a JSON file. The list is loaded from a file named `add_item.json`.
If the file does not exist, it initializes an empty list.
"""

import sys
import json

if __name__ == "__main__":
   
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
