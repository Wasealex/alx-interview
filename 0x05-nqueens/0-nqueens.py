#!/usr/bin/python3
"""
This module has a function `is_safe` that checks if placing a queen
on a given position in a chessboard is safe, ensuring no other queens
are in the same column or upper left diagonal.
"""
import sys


def is_safe(row, col, board):
    """
    Checks if it's safe to place a queen on the chessboard
      at the given row and column.

    Args:
        row (int): The row index where the queen is being placed.
        col (int): The column index where the queen is being placed.
        board (list): The current state of the chessboard,
          represented as a list of column indices.

    Returns:
        bool: True if the placement is safe, False otherwise.
    """
    # Check if the column is already occupied
    if col in board:
        return False

    # Check the upper left diagonal
    for i in range(row):
        if abs(board[i] - col) == row - i:
            return False

    return True


def solve_n_queens(n):
    """
    Solves the N-Queens problem by generating all possible solutions.

    Args:
        n (int): The number of queens (and the size of the chessboard).

    Returns:
        list: A list of all valid solutions, where each solution is a list.
    """
    solutions = [[]]  # Start with an empty solution

    for row in range(n):
        new_solutions = []
        for solution in solutions:
            for col in range(n):
                if is_safe(row, col, solution):
                    new_solutions.append(solution + [col])
        solutions = new_solutions

    return solutions


def main():
    """
    The main entry point of the program.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])


if __name__ == '__main__':
    main()
