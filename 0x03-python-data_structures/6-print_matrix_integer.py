#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for index, element in enumerate(i):
            print("{:d}".format(element), end=' ')
            if index == len(i) - 1:
                print()

