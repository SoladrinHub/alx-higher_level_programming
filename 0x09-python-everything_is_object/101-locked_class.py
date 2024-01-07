#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    prevent thuser from instantiating new LockedClass attributes
    """

    __slots__ = ["first_name"]
