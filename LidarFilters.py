"""Docstring to be filled
With stuff written
"""

import numpy as np


class RangeFilter(object):
    """stuff
    ddd
    """

    def __init__(self, low = 0.03, high = 50.0):
        self.range_min = low
        self.range_max = high

    def update(self, scan):
        filtered_scan = scan
        for i, value in enumerate(scan):
            if value < self.range_min:
                filtered_scan[i] = self.range_min
            if value > self.range_max:
                filtered_scan[i] = self.range_max
        return filtered_scan


class TemporalMedianFilter(object):
    """stuff
    ddd
    """

    def __init__(self, D = 0):
        self.num_scans_to_use = D + 1
        self.scans_to_use = []
        self.circular_index = 0

    def update(self, cur_scan):
        filtered_scan = []
        if len(self.scans_to_use) < self.num_scans_to_use:
            self.scans_to_use.append(cur_scan)
        else:
            self.scans_to_use[self.circular_index] = cur_scan
            self.circular_index =+ 1
            if self.circular_index == self.num_scans_to_use:
                self.circular_index = 0
        for i in range(len(cur_scan)):
            same_indexed_elements = list(value[i] for value in self.scans_to_use)
            filtered_scan.append(np.median(same_indexed_elements))
        return filtered_scan
