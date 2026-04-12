#!/usr/bin/env python3
""" Module for Task 7: Complex types - to_kv. """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple with the string k and the square of v as a float. """
    return (k, float(v**2))
