#!/usr/bin/python3
"""Module that defines a Square class with getter, setter, and area.

This module defines a Square class with a private size attribute. The
size can be accessed and modified using a property, with validation
for type and value. The class also provides a public method to compute
the area of the square.
"""


class Square:
    """Represent a square with a private size attribute.

    The size attribute is validated to be an integer >= 0. The class
    provides a getter and setter for size, as well as a method to
    calculate the square's area.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
