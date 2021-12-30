"""Quick and dirty testing of classes in module lidar_filters"""

from lidar_filters import TemporalMedianFilter, RangeFilter
import random

temp_med_filter = TemporalMedianFilter(4)
rang_filter = RangeFilter(3,7)

data = []
for i in range(1000):
    data.append(round(random.gauss(5,2.5)))

print(data)
print(temp_med_filter.update(data))
print()
for i in range(6):
    data = []
    for j in range(1000):
        data.append(round(random.gauss(5,2.5)))
    print(data)
    print(temp_med_filter.update(data))
    print()
