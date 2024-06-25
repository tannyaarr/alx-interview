#!/usr/bin/python3
"""returns the perimeter of the island"""


def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    land = 0
    shared_edges = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                land += 1
                if r < rows - 1 and grid[r + 1][c] == 1:
                    shared_edges += 1
                if c < cols - 1 and grid[r][c + 1] == 1:
                    shared_edges += 1
    
    return 4 * land - 2 * shared_edges
