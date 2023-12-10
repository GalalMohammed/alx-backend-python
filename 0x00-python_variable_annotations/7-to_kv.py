#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines to_kv function.

Example:
    print(to_kv("eggs", 3))

"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """a type-annotated function to_kv.

    Args:
        k (str): dummy arg.
        v (object): number to be squared.

    Returns:
        tuple.

    """
    return (k, v * v)
