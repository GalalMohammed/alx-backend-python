#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines async_comprehension.

Example:
    print(await async_comprehension())

"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers.

        Returns:
            list.

    """
    return [i async for i in async_generator()]
