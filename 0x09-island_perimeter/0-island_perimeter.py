#!/usr/bin/python3
"""returns the perimeter of the island"""


def island_perimeter(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1

    return perimeter
