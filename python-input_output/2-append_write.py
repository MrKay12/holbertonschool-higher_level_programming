#!/usr/bin/python3
"""Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """


def append_write(filename="", text=""):
    """Appends string end of text file and returns number characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
