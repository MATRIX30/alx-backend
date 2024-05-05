#!/usr/bin/env python3
"""
contains helper function for pagination
and Server class
"""


import csv
import math
from typing import List
from typing import Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Helper function to help in pagination
        Args:
                    page(int): page number
                    page_size: The size of the page
            Returns:
                    Tuple(int,int): returns a tuple of size 2 containing the
                    start and stop index corresponding to the range
                                    of indexes
                    List([]): empty list if page size is out of range
        """
        stop_index = 0
        for i in range(page):
            start_index = stop_index
            stop_index += page_size

        return (start_index, stop_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        if page_size > len(self.__dataset):
            return []
        start, stop = Server.index_range(page, page_size)
        return self.dataset()[start:stop]
