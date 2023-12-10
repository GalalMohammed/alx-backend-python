#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines make_multiplier function.

Example:
    fun = make_multiplier(2.22)

"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier.

    Args:
        multiplier (float): number to be multiplied by.

    Returns:
        function.

    """
    return lambda number: number * multiplier
