#!/usr/bin/python3
"""Method that determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """the initialization of canUnlockAll"""
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if 0 <= key < n:
                    stack.append(key)

    return len(visited) == n
