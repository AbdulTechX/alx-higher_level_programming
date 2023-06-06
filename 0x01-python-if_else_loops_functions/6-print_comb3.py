#!/usr/bin/python3
"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for number in range(0, 10):
    for alteration in range(number + 1, 10):
        if number == 8 and alteration == 9:
            print("{}{}".format(number, alteration))
        else:
            print("{}{}".format(number, alteration), end=", ")
