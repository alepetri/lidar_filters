"""Module contains lidar filters.

Imports Used:
numpy
Classes:
RangeFilter -- min/max limiting of data
TemporalMedianFilter -- approximate current data based on past data
"""

import numpy as np


class RangeFilter(object):
    """Objects perform min/max limiting of data.

    Methods:
    update -- pass scans through filter
    Instance variables:
    range_min -- (float) lower limit of range
    range_max -- (float) higher limit of range
    """

    def __init__(self, low = 0.03, high = 50.0):
        """Initialize instance variables to be used in filtering

        Keyword arguements:
        low -- (default=0.03) minmum value for filtered data
        high -- (default=50.0) maximum value for filtered data
        """
        self.range_min = low
        self.range_max = high

    def update(self, scan):
        """Do limit filtering and return filtered scan.

        Keyword argumenets:
        low -- the lower limit that the filter will return
        high -- the higher limit that the filter will return
        """
        filtered_scan = scan
        for i, value in enumerate(scan):
            if value < self.range_min:
                filtered_scan[i] = self.range_min
            if value > self.range_max:
                filtered_scan[i] = self.range_max
        return filtered_scan


class TemporalMedianFilter(object):
    """Objects perform temporal median filtering of data.

    Methods:
    update -- pass scans through filter
    Instance variables:
    num_scans_to_use -- (int) provides length of scans_to_use list
    scas_to_use -- (list) stores considered past scans for calculation
    circular_index -- (int) index of next scan to replace with new scan
    """

    def __init__(self, D = 0):
        """Initialize instance variables to be used in filtering.

        Keyword arguements:
        D -- (default: 0) the number of past scans the filter references
        """
        self.num_scans_to_use = D + 1
        self.scans_to_use = []
        self.circular_index = 0

    def update(self, cur_scan):
        """Do temperal median filtering and return filtered scan.

        Calculate median values of current and past D scans.
        Use circular indexing to save memory and complexity.
        Keyword arguements:
        cur_scan -- most recent unfiltered scan to be filtered
        """
        filtered_scan = []
        if len(self.scans_to_use) < self.num_scans_to_use:
            self.scans_to_use.append(cur_scan)
        else:
            self.scans_to_use[self.circular_index] = cur_scan
            self.circular_index =+ 1
            if self.circular_index == self.num_scans_to_use:
                self.circular_index = 0
        for i in range(len(cur_scan)):
            same_indexed_elements = list(value[i] for value in
                                         self.scans_to_use
                                         )
            filtered_scan.append(np.median(same_indexed_elements))
        return filtered_scan
