#!/usr/bin/env python3
"""Basic caching model"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """an object that stores and retrive data from dictionary"""
    def put(self, key, item):
        """store data to dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return specific data based on the key from dictionary"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
        """
        or use just a single line of code
        return self.cache_data.get(key, None)
        """
