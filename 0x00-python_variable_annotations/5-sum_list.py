#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines sum_list function.

Example:
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)

"""


def sum_list(input_list: list[float]) -> float:
    """a type-annotated function sum_list.

    Args:
        input_list (list): floats args.

    Returns:
        their sum.

    """
    return sum(input_list)
