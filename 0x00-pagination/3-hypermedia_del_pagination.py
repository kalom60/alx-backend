#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        function to make the user does not
        miss items from dataset when changing page
        """
        assert index is not None and \
               index >= 0 and \
               index < len(self.__indexed_dataset)
        data = []
        starter = index
        nxt_page = 0
        count = 0
        for i, value in self.__indexed_dataset.items():
            if i >= starter and count < page_size:
                data.append(value)
                count += 1
            elif count == page_size:
                nxt_page = i
                break
        return {
                'index': index,
                'data': data,
                'page_size': page_size,
                'next_index': nxt_page
                }
