#!/usr/bin/python3
"""Module defining the Square class with size validation and area.

This module provides a Square class with a private size attribute,
validates its value, and provides a method to compute the area.
"""


class Square:
    """Represent a square with a private size attribute.

    The size attribute is validated to be an integer >= 0. The class
    provides a method to calculate the square's area.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area.

        Returns:
            int: The area of the s
