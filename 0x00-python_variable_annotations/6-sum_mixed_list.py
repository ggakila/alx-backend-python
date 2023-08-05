#!/usr/bin/env python3
'''
Complex types - mixed list
'''
from typing import List, Union


num = Union[int, float]


def sum_mixed_list(mxd_lst: List[num]) -> float:
    '''
    accept int and floats return total in floats
    '''
    result: float = 0
    for x in mxd_lst:
        result += x
    return result
