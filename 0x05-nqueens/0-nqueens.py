#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            line = ''.join('Q' if col == row[i] else '.' for i, col in enumerate(range(len(row)))
            print(line)
        print()

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []

    def solve(row):
        if row == n:
            solutions.append(board[:])
        else:
            for col in range(n):
                if is_safe(board, row, col, n):
                    board[row] = col
                    solve(row + 1)
                    board[row] = -1

    solve(0)

    print_solutions(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)

