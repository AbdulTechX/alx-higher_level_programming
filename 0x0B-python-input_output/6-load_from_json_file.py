#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Read an object in python from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
