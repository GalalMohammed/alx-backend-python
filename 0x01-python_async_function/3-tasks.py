#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines task_wait_random function.

Example:
    task = task_wait_random(max_delay)

"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function.

    Args:
        max_delay (int): included arg.

    Returns:
        asyncio task.

    """
    return asyncio.create_task(wait_random(max_delay))
