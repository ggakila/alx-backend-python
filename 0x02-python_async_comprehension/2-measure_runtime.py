#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''
import asyncio
import time
asynced = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Running comprehension parellel 4 times'''
    start_time = time.time()
    await asyncio.gather(asynced(), asynced(), asynced(), asynced())
    end_time = time.time()
    return (end_time - start_time)
