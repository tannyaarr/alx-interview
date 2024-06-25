#!/usr/bin/python3
"""returns the perimeter of the island"""


def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    land_cells = 0
    shared_edges = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                land_cells += 1
                if c < cols - 1 and grid[r][c + 1] == 1:
                    shared_edges += 1
                if r < rows - 1 and grid[r + 1][c] == 1:
                    shared_edges += 1
    
    perimeter = 4 * land_cells - 2 * shared_edges
    return perimeter
