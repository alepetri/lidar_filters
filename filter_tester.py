from LidarFilters import TemporalMedianFilter, RangeFilter
import numpy as np

temp_med_filter = TemporalMedianFilter(3)
rang_filter = RangeFilter(1.3,3.6)


print(temp_med_filter.update([0, 1, 2, 1, 3]))
print(temp_med_filter.update([1, 5, 7, 1, 3]))
print(temp_med_filter.update([2, 3, 4, 1, 0]))
print(temp_med_filter.update([3, 3, 3, 1, 3]))
print(temp_med_filter.update([10, 2, 4, 0, 0]))

print(rang_filter.update([0, 1, 2, 1, 3]))
print(rang_filter.update([1, 5, 7, 1, 3]))
print(rang_filter.update([2, 3, 4, 1, 0]))
print(rang_filter.update([3, 3, 3, 1, 3]))
print(rang_filter.update([10, 2, 4, 0, 0]))
