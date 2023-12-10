#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines sum_mixed_list function.

Example:
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)

"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """a type-annotated function sum_mixed_list.

    Args:
        mxd_lst (list): args.

    Returns:
        their sum.

    """
    return sum(mxd_lst)
