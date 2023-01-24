#!/usr/bin/python3
""" create class square with attribute validation"""


class Square:
    """ square class """

    def __init__(self, size=0):
        """ initialize atributes """
        self.__size = size

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
