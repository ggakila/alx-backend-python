#!/usr/bin/env python3
'''
sum_list fuction takes a list input_list of floats as argument and
returns their sum as a float.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Returns sum of list
    '''
    result: float = 0
    for x in input_list:
        result += x
    return result
