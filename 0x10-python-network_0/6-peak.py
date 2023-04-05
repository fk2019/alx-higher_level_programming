#!/usr/bin/python3
"""Find peak in alit of unsorted integers
"""


def find_peak(list_of_integers):
    """Function to find peak in an unsorted list of integers
    """
    if (len(list_of_integers) == 0):
        return (None)
    down = 0
    up = len(list_of_integers) - 1
    while down < up:
        center = (down + up) // 2
        if (list_of_integers[center] < list_of_integers[center + 1]):
            down = center + 1
        else:
            up = center
    return (list_of_integers[down] or list_of_integers)
