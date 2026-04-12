#!/usr/bin/env python3
""" Module for Task 9: Duck type an iterable. """
from typing import Iterable, Sequence, List, Tuple


def element_length(elts: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples containing elements and their lengths. """
    return [(i, len(i)) for i in elts]
