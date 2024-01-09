#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """check is an object is an instance or an inherited instance of a class.

    Args:
        obj (any): the object to check
        a_class (type): class
    Returns:
        if obj is an instance or inherited instanceof a_class - True
        otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
