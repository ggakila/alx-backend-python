#!/usr/bin/env python3
'''Running multiple coroutines'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''executing multiple coroutines with async'''
    delays: List[float] = []
    final_delayList: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        first_in = await(delay)
        final_delayList.append(first_in)
    return final_delayList
