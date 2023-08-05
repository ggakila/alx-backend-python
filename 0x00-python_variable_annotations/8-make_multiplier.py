#!/usr/bin/env python3
'''
 Complex types - functions
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returning functions i.e. collables
    '''
    def x(f: float) -> float:
        """ The callable function being returned """
        return float(f * multiplier)

    return x
