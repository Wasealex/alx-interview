#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    return: Nothing. The matrix must be edited in-place.
    """
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]  # Save current cell
            matrix[i][j] =  matrix[n - 1 - j][i]  # Move from right to top
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]  # Move from bottom to right
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]  # Move from left to bottom
            matrix[j][n - 1 - i] = temp

    return matrix
