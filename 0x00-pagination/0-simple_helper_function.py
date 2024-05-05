#!/usr/bin/env python3
"""
contains helper function for pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Helper function to help in pagination
    Args:
                page(int): page number
                page_size: The size of the page
        Returns:
                Tuple(int,int): returns a tuple of size 2 containing the
                                start and stop index corresponding to the range
                                of indexes
    """
    stop_index = 0
    for i in range(page):
        start_index = stop_index
        stop_index += page_size

    return (start_index, stop_index)
