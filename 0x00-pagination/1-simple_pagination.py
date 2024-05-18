#!/usr/bin/env python3
"""This module contains 1 helper function"""
import csv
import math
from typing import List


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset
        args:
            page -> int: the page number
            page_size -> int: the size of the page
        returns:
            List of lists representing the page of data
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page_size > 0 and page > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]
