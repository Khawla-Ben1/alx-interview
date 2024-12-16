#!/usr/bin/python3
"""
returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Returns: The perimeter of the island .
    """


    nbr_row = len(grid)
    nbr_col = len(grid[0])
    perimeter = 0
    for row in range(nbr_row):
        for col in range(nbr_col):
            # Check if current cell is land, add 4 to the perimeter
            if grid[row][col] == 1:
                perimeter += 4
                # if current cell is also land & not on the grid's edge
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # minus 2 from d perimeter(shared side)
                # Check if the cell to the left is also land
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # minus 2 from d perimeter(shared side)
    return perimeter
