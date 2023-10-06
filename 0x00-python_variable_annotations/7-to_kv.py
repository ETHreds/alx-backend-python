#!/usr/bin/env python3
"""
function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple
"""


from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing the string k and the square of int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v as a float.
    """
    return (k, float(v ** 2))
