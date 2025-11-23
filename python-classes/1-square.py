#!/usr/bin/python3
"""Module that defines a Square class with size validation.

This module defines a Square class with a private size attribute. The
size is validated to be an integer >= 0. No external modules are imported.
"""


class Square:
    """Represent a square with a private size attribute.

    The size attribute is validated to ensure type and value correctness.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

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
