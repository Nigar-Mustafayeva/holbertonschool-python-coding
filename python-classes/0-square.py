#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute.

This module provides a basic Square class used for later exercises
in the python-classes project.
"""


class Square:
    """Represent a square with a private size attribute.

    The attribute is stored privately so the class creator can
    control access and validation in later tasks.
    """

    def __init__(self, size):
        """Initialize a new Square with the given size.

        Args:
            size (any): The initial size of the square (no validation required).
        """
        self.__size = size
