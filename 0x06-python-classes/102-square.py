#!/usr/bin/python3
""" create class square with attribute validation"""


class Square:
    """ square class """

    def __init__(self, size=0):
        """ initialize atributes """
        self.__size = size

    def __lt__(self, other):
        """ check less  than comparision """
        return self.area() < other.area()

    def __le__(self, other):
        """check less than or equal to"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """checks equality"""
        return self.area() == other.area()

    def __ne__(self, other):
        """checks non equality"""
        return self.area() != other.area()

    def __gt__(self, other):
        """checks greater than comparision"""
        return self.area() > other.area()

    def __ge__(self, other):
        """checks greater than or equals to  comparision"""
        return self.area() >= other.area()

    @property
    def size(self):
        """ get/retrive value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the value of size"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ return sqaure of size """
        return (self.__size ** 2)
