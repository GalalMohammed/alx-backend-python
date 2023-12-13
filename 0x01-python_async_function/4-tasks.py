#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines task_wait_n function.

Example:
    print(asyncio.run(task_wait_n(n, max_delay)))

"""


from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times.

    Args:
        n (int): no of times.
        max_delay (int): included arg.

    Returns:
        sorted delays.

    """
    d = await asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])
    return sorted(d)
