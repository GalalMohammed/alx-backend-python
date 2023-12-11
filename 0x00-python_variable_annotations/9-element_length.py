#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines element_length function.

Example:
    print(element_length.__annotations__)

"""


from collections.abc import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> list[tuple[Sequence, int]]:
    """Element length computer.

    Args:
        lst (object): list to be used.

    Returns:
        list.
    """
    return [(i, len(i)) for i in lst]
