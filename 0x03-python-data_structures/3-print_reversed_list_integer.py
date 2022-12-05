#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list)
    while (idx > 0):
        print("{:d}".format(idx))
        idx -= 1
