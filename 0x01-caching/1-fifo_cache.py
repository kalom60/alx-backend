#!/usr/bin/env python3
"""First In First Out caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    an object that stores and retrive a data from a dictionary
    and use FIFO system to remove when it reachs its limit
    """
    def __init__(self):
        """Initialize cache"""
        super().__init__()

    def put(self, key, item):
        """
        store data to the dict and also check if
        it reachs its limit and perform FIFO
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = self.get_first_item()
            self.cache_data.pop(key)
            print(f'DISCARD: {key}')

    def get_first_item(self):
        """return the first key from the dict"""
        for key in self.cache_data.keys():
            return key

    def get(self, key):
        """return a data based on its key"""
        return self.cache_data.get(key, None)
