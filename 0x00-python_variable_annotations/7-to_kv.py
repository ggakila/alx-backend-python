#!/usr/bin/env python3
'''
Complex types - string and int/float to tuple
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Tuple typing
    '''
    result: Tuple(str, Union[int, float])
    result = (k, v**2)
    return result
