#!/usr/bin/env python3
"""
This module is an implementation of a simple
LFU least frequently used caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    This is a class for a LFU caching system
    inheriting from BaseCaching
    """
    def __init__(self):
        """
        Initialization method for the class
            cache_data: dict {}
        from the parent class BaseCaching
        """
        super().__init__()
        self.cache_order = []
        self.cache_usage = {}

    def put(self, key, item):
        """
        This method adds a new item to the dictionary
        and removes the least frequently used item to make way for new ones.
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                discard = self.cache_order.pop(0)
                del self.cache_data[discard]
                del self.cache_usage[discard]
                print(f"DISCARD: {discard}")
            self.cache_data[key] = item
            self.cache_order.append(key)
            self.cache_usage[key] = 0

    def get(self, key):
        """
        This method returns the value item from
        the key value pair in the cache_data dict
        args:
            key: str
        returns: the value pair else None
        """
        if key in self.cache_data:
            self.cache_usage[key] += 1
            self.cache_order.remove(key)
            self.cache_order.append(key)
        return self.cache_data.get(key)
