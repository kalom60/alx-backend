#!/usr/bin/env python3
"""Last In First Out caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    an object that stores and retrive a data from a dictionary
    and use LIFO system to remove when it reachs its limit
    """
    def __init__(self):
        """Initialize cache"""
        super().__init__()

    def put(self, key, item):
        """
        store data to the dict and also check if
        it reachs its limit and perform LIFO
        """
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem()
            print(f'DISCARD: {last_key}')
        self.cache_data[key] = item

    def get(self, key):
        """return data based on its key"""
        return self.cache_data.get(key, None)
