#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute,
including getter and setter with validation.
"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the square with optional size."""
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
