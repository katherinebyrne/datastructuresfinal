#Katherine Byrne

import statistics
from statistics import stdev
dataset = []
i = 1


example1 = [79, 78, 78, 79, 77, 78, 78, 77, 78]
example2 = [68.2, 68, 69.0004, 68, 69.8, 70.123, 72, 73.10009, 74, 75.0]
i = i + 1

print("The Standard Deviation of Example 1 is % s" %(stdev(example1)))
std = statistics.stdev(example1)
if std < 1.0:
    print("COMFY")
else:
    print("NOT COMFY")

print("The Standard Deviation of Example 2 is % s" %(stdev(example2)))
std = statistics.stdev(example2)
if std < 1.0:
    print("COMFY")
else:
    print("NOT COMFY")


