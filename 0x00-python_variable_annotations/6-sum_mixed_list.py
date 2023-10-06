#!/usr/bin/env python3
"""
function sum_mixed_list which takes a list
returns  its sum
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Arg- Mixed list of int and floats
    returns- sum as float"""
    return float(sum(mxd_lst))
