#!/usr/bin/env python3
"""Task 8 module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a multiplier function"""
    def func(n: float) -> float:
        """Inner function"""
        return n * multiplier
    return func
