#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module defines concat function.

Example:
    print(concat(str1, str2) == "{}{}".format(str1, str2))

"""


def concat(str1: str, str2: str) -> str:
    """type-annotated function concat.

    Args:
        str1 (str): first arg.
        str2 (str): second arg.

    Returns:
        concatenated string.

    """
    return str1 + str2
