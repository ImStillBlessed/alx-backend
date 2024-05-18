#!/usr/bin/env python3
"""This module contains 1 helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    This function calculates the number of indexes
    in a page of values
    args:
        page -> int: the page munber.
        page_size -> int: number of indexes in each page
    returns:
        tuple of the page and page_size
    """
    finish = page * page_size
    start = finish - page_size
    return (start, finish)
