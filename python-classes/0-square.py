#!/usr/bin/python3
"""Module defining the Square class used in the python-classes project.

This module provides a basic implementation of a Square with a private
size attribute. The attribute is stored privately so that validation
and controlled access can be introduced in later tasks.
"""


class Square:
    """Represent a square with a private size attribute.

    The size attribute is stored privately to allow future validation
    and controlled access by the class.
    """

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (any): The initial size of the square (no validation yet).
        """
        self.__size = size
