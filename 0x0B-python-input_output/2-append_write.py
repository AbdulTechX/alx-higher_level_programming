#!/usr/bin/python3
# AbdulTechX
# 2-append_write.py
"""Write a function that appends a file"""


def append_write(filename="", text=""):
    """ appen  a string to utf8 text file.

    Args:
        filename (str): the name of the file to write.
        text (str): The text to write to the file.
    Return:
         The number of characters written:
    """
    with open(filename, 'a', encoding="UTF-8") as file:
        return file.write(text)
