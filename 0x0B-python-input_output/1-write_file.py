#!/usr/bin/python3
# AbdulTechX
# 1-write_file.py
"""Define Function that write a string to a text_file
and return the number
"""


def write_file(filename="", text=""):
    """ Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Return:
         The number of characters written:
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return(file.write(text))
