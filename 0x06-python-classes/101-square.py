#!/usr/bin/python3
""" create class square with attribute validation"""


class Square:
    """ square class """

    def __init__(self, size=0, position=(0, 0)):
        """ initialize atributes """
        self.__size = size
        self.__position = position

    def __str__(self):
        """Prints a square made of `#`"""
        square = []
        if self.__size == 0:
            return ""
        [square.append("\n") for i in range(self.position[1])]
        for i in range(self.__size):
            for j in range(self.__position[0]):
                square.append(" ")
            for k in range(self.__size):
                square.append("#")
            if i < (self.__size - 1):
                square.append("\n")
        return "".join(square)

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

    @property
    def position(self):
        """retrive value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ set value of position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return sqaure of size """
        return (self.__size ** 2)

    def my_print(self):
        """print square made of #"""
        if self.__size == 0:
            print()
            return
        else:
            [print() for i in range(self.position[1])]
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
