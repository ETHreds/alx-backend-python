#!/usr/bin/env python3
"""
Annotated variables
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input iterable and return the results as a list of tuples.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains two elements:
        - The first element is a sequence from the input iterable.
        - The second element is an integer representing the length of the sequence.

    """
    return [(i, len(i)) for i in lst]
