#!/usr/bin/python3
"""
a module that contains one function island_perimeter(grid)
grid is a list of list of integers
"""


def island_perimeter(grid):
    """Parameters: grid (List[List[int]]): A 2D list where:
                                            0 represents water.
                                            1 represents land.
    The grid is guaranteed to be rectangular. 
    The island is completely surrounded by water, 
    and there is only one island (or none). 
    There are no lakes within the island.

    Returns
            int: The perimeter of the island. 
            The perimeter is calculated based on 
            the number of exposed sides of 
            the land cells (1s) in the grid.
    """
    if not grid:
        return 0
    
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides
                perimeter += 4
                
                # Subtract for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Down
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Right
                    perimeter -= 1
    
    return perimeter
