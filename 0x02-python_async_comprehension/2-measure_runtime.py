#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines measure_runtime.

Example:
    await(measure_runtime())

"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine will execute async_comprehension four times in parallel.

        Returns:
            total runtime.

    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - start
