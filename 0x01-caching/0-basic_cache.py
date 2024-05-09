#!/usr/bin/env python3
"""
Basic Caching Module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class contains implementation for basic
    caching mechanism
    """

    def __init__(self):
        """
        constructor of base_caching
        """
        super().__init__()

    def put(self, key, item):
        """
        put method to put data into caching system
        """
        if not ((key is None) or (item is None)):
            self.cache_data[key] = item

    def get(self, key):
        """
        Method to get data from caching system
        """
        if (key not in self.cache_data.keys()) or key is None:
            return None
        return self.cache_data[key]
