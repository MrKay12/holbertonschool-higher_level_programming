#!/usr/bin/python3
"""
    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """


def write_file(filename="", text=""):
    """Writes string to text file (UTF8) returns number of characters"""
    with open(filename, encoding='utf-8') as f:
        return f.write(text)
