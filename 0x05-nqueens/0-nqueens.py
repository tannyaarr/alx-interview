#!/usr/bin/python3
""""N queen puzzle is a challenge pf placing N non-attacking
quuens on an NxN chessboard"""


import sys


def print_usage_and_exit(message):
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board, n)
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1


def print_solution(board, n):
    solution = [[i, board[i]] for i in range(n)]
    print(solution)


def nqueens(n):
    if not isinstance(n, int):
        print_usage_and_exit("N must be a number")
    if n < 4:
        print_usage_and_exit("N must be at least 4")

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    nqueens(N)