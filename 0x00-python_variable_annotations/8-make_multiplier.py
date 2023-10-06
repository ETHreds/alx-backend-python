#!/usr/bin/env python3
"""
Doc String
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used by the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
