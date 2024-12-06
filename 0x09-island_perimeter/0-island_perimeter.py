#!/usr/bin/python3
"""
Island perimeter problem.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid
    Args:
        grid (List[List[int]]): 2D grid where 1 represents
        land and 0 represents water
    Returns:
        int: The perimeter of the island
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 sides of current land cell
                # Top neighbor
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Bottom neighbor
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left neighbor
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right neighbor
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter

