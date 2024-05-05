#!/usr/bin/env python3
"""
contains helper function for pagination
and Server class
"""
import csv
import math
from typing import Tuple, List, Dict


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
        """
        method to get the range of pages to return as a list of list
        Args:
            page(int): number of pages to return
            page_size(int): size of data per page
        Returns:
                List(List): a list of list data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        if page_size > len(self.__dataset):
            return []
        start, stop = Server.index_range(page, page_size)
        return self.dataset()[start:stop]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
         get_hyper method to return the
        Args:
            page(int): number of pages to return
            page_size(int): size of data per page

        Returns:
            Dict():{
                page_size(int): the length of the returned
                dataset page
                page(int): the current page number
                data(List(List)): the dataset page
                (equivalent to return from previous task)
                next_page(int): number of the next page,
                None if no next page
                prev_page(int): number of the previous page,
                None if no previous page
                total_pages(int): the total number of pages
                in the dataset as an integer
                }
        """

        hyper_data = {}
        hyper_data["page_size"] = page_size if self.get_page(page,
                                                             page_size) else 0
        hyper_data["page"] = page
        hyper_data["data"] = self.get_page(page, page_size)
        hyper_data["next_page"] = page + 1 if self.get_page(
            page, page_size) else None
        hyper_data["prev_page"] = page - 1 if page - 1 > 0 else None
        hyper_data["total_pages"] = math.ceil(len(self.dataset()) / page_size)
        return hyper_data
