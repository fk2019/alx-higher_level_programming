#!/usr/bin/python3
"""Module returns the object represented by JSON string
"""
import json


def from_json_string(my_str):
    """Returns JSON representation of object(string)"""
    return json.loads(my_str)
