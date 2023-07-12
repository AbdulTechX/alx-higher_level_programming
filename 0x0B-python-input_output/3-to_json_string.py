#!/usr/bin/python3
# AbdulTechX
# 3-to_json_string.py
"""Write a function that returns the JSON
representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """return JSON representation of an object"""
    return json.dumps(my_obj)
