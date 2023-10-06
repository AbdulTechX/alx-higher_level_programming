#!/usr/bin/python3
# Write a function that finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):
    if not list_of_integers:
        return None  # Return None if the list is empty

    for i in range(len(list_of_integers)):
        # Check if the current element is greater than its neighbors (if they exist)
        if (i == 0 or list_of_integers[i] >= list_of_integers[i - 1]) and (i == len(list_of_integers) - 1 or list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]  # Found a peak, return iti
        return None
