#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """function that prints all integers of a list."""
    for index in range(len(my_list)):
        i = 0
        if i <= index:
            print("{:d}".format(my_list[index]))
