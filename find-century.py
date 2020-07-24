"""
Given a year, return the century it is in. 
The first century spans from the year 1 up to and 
including the year 100, the second - from the year 
101 up to and including the year 200, etc.
"""

import math

def century(year):
    return math.ceil(year/100)

print("Year : 1901, Century :", century(1901))
print("Year : 1900, Century :", century(1900))
print("Year : 1984, Century :", century(1984))
print("Year : 2020, Century :", century(2020))