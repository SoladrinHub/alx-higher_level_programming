#!/usr/bin/python3

""" Define a class square"""


class Square:
    """ this is a square class"""
    def __init__(self, size=0):
        """initialize a new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self._size = size
