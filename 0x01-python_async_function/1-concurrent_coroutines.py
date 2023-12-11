#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines wait_n function.

Example:
    print(asyncio.run(wait_n(5, 5)))

"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n :int, max_delay: int) -> list[float]:
    """Spawn wait_random n times.

    Args:
        n (int): no of times.
        max_delay (int): included arg.

    Returns:
        sorted delays.

    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    delays.sort()
    return delays
