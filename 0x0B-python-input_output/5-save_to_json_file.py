#!/usr/bin/python3
# AbdulTechX
# 5-save_to_json_file.py
"""Write a function that writes an Object to a text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """"Writeobject to a text file

    Args:
       filename(obj): the name of the file to write.
       obj: The object to write to file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
