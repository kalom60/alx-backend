#!/usr/bin/env python3
"""Most Recently Used caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    an object that stores and retrive a data from a dictionary
    and use MRU system to remove when it reachs its limit
    """
    def __init__(self):
        """initialize cache"""
        super().__init__()

    def put(self, key, item):
        """
        store data to the dict and also check if
        it reachs its limit and perform MRU
        """
        if key is not None and item is not None:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    last_key, _ = self.cache_data.popitem()
                    print(f'DISCARD: {last_key}')
                    self.cache_data[key] = item
                else:
                    self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """return data based on its key"""
        if key is not None and key in self.cache_data:
            item = self.cache_data.get(key)
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return self.cache_data.get(key, None)
        return None
