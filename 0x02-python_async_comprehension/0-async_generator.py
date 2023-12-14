#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines async_generator.

Example:
    result = []
    async for i in async_generator():
        result.append(i)

"""


import random
import asyncio
from collections.abc import Iterator


async def async_generator() -> Iterator[float]:
    """The coroutine will loop 10 times,
        each time asynchronously wait 1 second.

        Yields:
            float: The next random number between 0 and 10

        Examples:
            >>> print([i async for i in async_generator()])
            [
                    4.403136952967102, 6.9092712604587465, 6.293445466782645,
                    4.549663490048418, 4.1326571686139015, 9.99058525304903,
                    6.726734105473811, 9.84331704602206, 1.0067279479988345,
                    1.3783306401737838
                    ]

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
