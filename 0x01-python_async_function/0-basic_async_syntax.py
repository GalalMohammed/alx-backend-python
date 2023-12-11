#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines wait_random function.

Example:
    print(asyncio.run(wait_random()))

"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay.

    Args:
        max_delay (int): included arg.

    Returns:
        float.

    """
    async_delay = random.uniform(0, max_delay)
    await asyncio.sleep(async_delay)
    return async_delay
