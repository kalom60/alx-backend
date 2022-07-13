#!/usr/bin/env python3
"""Least Frequently Used caching system"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    an object that stores and retrive a data from a dictionary
    and use LFU system to remove when it reachs its limit
    """
    def __init__(self):
        """initialize cache"""
        super().__init__()
        self.uses = {}

    def put(self, key, item):
        """
        store data to the dict and also check if
        it reachs its limit and perform LFU
        """
        keys = []
        if key is not None and item is not None:
            if (len(self.cache_data) < BaseCaching.MAX_ITEMS):
                self.cache_data[key] = item
            else:
                if (key in self.cache_data):
                    self.cache_data[key] = item
                else:
                    for i in sorted(self.cache_data.keys()):
                        if i not in self.uses:
                            keys.append(i)
                    if self.cache_data.keys() == self.uses.keys():
                        keys.append(list(self.cache_data.keys())[0])
                    first_key = keys[0]
                    print(f'DISCARD: {first_key}')
                    self.cache_data.pop(first_key)
                    self.cache_data[key] = item

    def get(self, key):
        """return data based on its key"""
        if key is not None and key in self.cache_data:
            item = self.cache_data.get(key)
            if key not in self.uses:
                self.uses[key] = item
            return self.cache_data.get(key)
        return None
