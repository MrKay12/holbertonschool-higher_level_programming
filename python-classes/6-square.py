#!/usr/bin/python3
"""Define a class for Square"""


class Square:
    """
    Class that represents a square.

    Attributes:
    ----------
    size : int
        The size of one side of the square (must be an integer >= 0).

    position : tuple
        The position of the square when printed
        (must be a tuple of two positive integers).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with optional size and position.

        Parameters:
        ----------
        size : int, optional
            The size of one side of the square (default is 0).

        position : tuple, optional
            The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
        -------
        int
            The current size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.
        Ensures the size is a non-negative integer.

        Parameters:
        ----------
        value : int
            The size of the square to be set.

        Raises:
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Getter for the position of the square.

        Returns:
        -------
        tuple
            The current position of the square
            (horizontal and vertical offset).
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.
        Ensures position is a tuple of two positive integers.

        Parameters:
        ----------
        value : tuple
            A tuple with two positive integers
            representing the position of the square.

        Raises:
        ------
        TypeError
            If position is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        -------
        int
            The area of the square.
        """
        return self._size * self._size

    def my_print(self):
        """
        Prints the square using the '#' character.
        The position is respected with spaces.

        If the size is 0, an empty line is printed.
        """
        if self._size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()

            for _ in range(self.size):
                print("_" * self._position[0] + "#" * self.size)
