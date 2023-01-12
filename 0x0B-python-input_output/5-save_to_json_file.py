#!/usr/bin/python3
"""Module writes an Object to a text file using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes my_object to filename using JSON representation"""
    with open(filename, mode="w", encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
