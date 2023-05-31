#!/usr/bin/python3
"""This module is to write a class object Square"""


class Square:
    """Represents Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize self method and size attribute"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Preperty setter"""
        self.value = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """property to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter"""
        self.value = value
        if (not isinstance(value, tuple) or len(value) != 2 or not all (isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """public instance methed that return square area"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """
        public instance methed that prints in stdout the square
        """
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for m in range(self.__size):
                    print("#", end="")
                print()
