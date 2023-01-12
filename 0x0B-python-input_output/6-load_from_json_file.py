#!/usr/bin/python3
"""Module creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """Creates object from filename"""
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    return data
