#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    if list_of_integers:
        low = 0
        high = len(list_of_integers)
        while low < high:
            mid = low + (high - low) // 2
            mid = int(mid)
            if high == 1:
                return list_of_integers[0]
            if high == 2:
                return max(list_of_integers)
            if list_of_integers[mid] >= list_of_integers[mid - 1] and\
               list_of_integers[mid] >= list_of_integers[mid + 1]:
                return list_of_integers[mid]
            if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
                return find_peak(list_of_integers[mid:])
            if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
                return find_peak(list_of_integers[:mid])
    else:
        return None
