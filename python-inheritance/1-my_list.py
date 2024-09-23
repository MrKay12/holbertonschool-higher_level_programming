#!/usr/bin/python3
"""A class MyList which inherits the list"""


class MyList(list):
    """Class MyList inherits list"""

    def print_sorted(self):
        """Prints the list ascending sorted order"""
        print(sorted(self))
