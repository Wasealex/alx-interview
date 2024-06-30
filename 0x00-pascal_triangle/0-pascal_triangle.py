#!/usr/bin/python3
"""Module Pascal Triangle"""


def pascal_triangle(n):
    """Definition of Pascal Triangle.
    Returns a list of lists representing the Pascal Triangle of size n.
    Returns an empty list if n < 0.
    """
    pascal = []
    if n <= 0:
        return pascal

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(row)

    return pascal
