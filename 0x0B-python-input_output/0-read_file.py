#!/usr/bin/python3
# AbdulTechX
# 0-read_file
"""Define Function that reads text_file"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
