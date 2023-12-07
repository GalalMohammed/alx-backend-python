#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines to_str function.

Example:
    pi_str = to_str(3.14)

"""


def to_str(n: float) -> str:
    """type-annotated function to_str.

    Args:
        n (float):  number.

    Returns:
        str repr of float.

    """
    return repr(n)
