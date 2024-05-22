#!/usr/bin/env python3
"""
This module is an implementation of a simple caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    This class is a basic cache system with no limits
    """
    def __init__(self):
        """
        Initialization method for the class
            cache_data: dict {}
        from the parent class BaseChaching
        """
        super().__init__()

    def put(self, key, item):
        """
        This method assigns items to keys in the cache_data
        dict
        args:
            key: str
            item: any
        if key or item is None do nothing
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        This method returns the value item from
        the key value pair in the cache_data dict
        args:
            key: str
        returns: the value pair else None
        """
        return self.cache_data.get(key)
