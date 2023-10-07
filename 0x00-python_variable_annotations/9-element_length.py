#!/usr/bin/env python3
"""
Calculate the length of each element in the input
iterable and return the results as a list of tuples.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequences (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains two elements:
   """
    return [(i, len(i)) for i in lst]
