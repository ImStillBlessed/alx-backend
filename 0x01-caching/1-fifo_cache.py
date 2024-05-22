#!/usr/bin/env python3
"""
This module is an implementation of a simple
FIFO first in first out caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """This is a class for a FIFO caching system
    inherits BaseChing
    """
    def __init__(self):
        """
        Initialization method for the class
            cache_data: dict {}
        from the parent class BaseChaching
        """
        super().__init__()

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                discard = key
                if key not in self.cache_data.keys():
                    discard = next(iter(self.cache_data))
                    print(f"DISCARD: {discard}")
                removed_key = self.cache_data.pop(discard)
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
