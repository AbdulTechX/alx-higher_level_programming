#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers."""
    for idx in range(len(matrix)):
        for i in range(len(matrix[idx])):
            print("{:d}".format(matrix[idx][i]), end="")
            if i != (len(matrix[idx]) - 1):
                print(" ", end="")
        print("")
