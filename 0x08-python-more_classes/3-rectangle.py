#!/usr/bin/python3
# 3-rectangle.py
# AbdulTechX
"""Define a Rectangle class"""


class Rectangle:
    """"Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """initializing anew square.

        Args:
            width (int): The width of the new Rectangle
            height (int): the hieght of the new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the rectangle."""
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of the rectangle"""
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <0:
            raise TypeError("height msut be >= 0")
        self.__height = value

    def area(self):
        """Return the Area of the rectangle."""
        return(self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Retangle"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable representation

        Represents the rectangle with the # charcter
        """
        if self.__width == 0 or self.height == 0:
            return("")
        rect = []
        for i in range(self.height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height -1:
                rect.append("\n")
        return ("".join(rect))
