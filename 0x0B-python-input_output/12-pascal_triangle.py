#!/usr/bin/python3
"""module utility function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    
    If n <= 0, returns an empty list.
    Assumes n will always be an integer.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    for c in range(1, n):
        row = [1]
        last_row = triangle[-1]
        for m in range(len(last_row) - 1):
            l = last_row[m] + last_row[m + 1]
            row.append(l)
        row.append(1)
        triangle.append(row)
    
    return triangle
