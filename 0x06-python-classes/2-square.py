#!/usr/bin/python3
# 2-square.py by AbdulTechX
"""Define a square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """Initializing this square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
