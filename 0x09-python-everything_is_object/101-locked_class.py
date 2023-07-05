#!/usr/bin/python3
""" Defines class LockedClass where the only new
instance attribute allowed is first_name """


class LockedClass:
    """ empty Class """
    __slots__ = ["first_name"]
