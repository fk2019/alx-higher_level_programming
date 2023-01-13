#!/usr/bin/python3
"""MModule adds all arguments to a Python list and save to a file
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []

if os.path.exists(filename):
    load_from_json_file(filename)

my_list = my_list + sys.argv[1:]
print(my_list)
save_to_json_file(my_list, filename)
