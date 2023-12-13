#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines measure_time function.

Example:
    print(measure_time(n, max_delay))

"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time.

    Args:
        n (int): no of times.
        max_delay (int): included arg.

    Returns:
        total time / n.

    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start) / n
