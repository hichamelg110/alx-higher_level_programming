#!/usr/bin/python3
"""This module solves the N-queens problem.

Finds all possible solutions to place N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N should be an integer that is 4 or more.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    all_solutions (list): A list of lists containing all solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen is placed on the chessboard.
"""
import sys


def create_board(n):
    """Create an `n`x`n` sized chessboard filled with 0's."""
    chessboard = []
    [chessboard.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chessboard]
    return chessboard


def copy_board(chessboard):
    """Create a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(copy_board, chessboard))
    return chessboard


def find_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_invalid_positions(chessboard, row, col):
    """Mark invalid spots on a chessboard.

    All spots where non-attacking queens can no
    longer be placed are marked.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    # Mark all forward spots
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # Mark all backwards spots
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # Mark all spots below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    # Mark all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    # Mark all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1
    # Mark all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def solve_n_queens(chessboard, row, queens, all_solutions):
    """Recursively solve the N-queens problem.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        all_solutions (list): A list of lists of all solutions.
    Returns:
        all_solutions
    """
    if queens == len(chessboard):
        all_solutions.append(find_solution(chessboard))
        return all_solutions

    for c in range(len(chessboard)):
        if chessboard[row][c] == " ":
            temp_chessboard = copy_board(chessboard)
            temp_chessboard[row][c] = "Q"
            mark_invalid_positions(temp_chessboard, row, c)
            all_solutions = solve_n_queens(temp_chessboard, row + 1,
                                        queens + 1, all_solutions)

    return all_solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = create_board(int(sys.argv[1]))
    all_solutions = solve_n_queens(chessboard, 0, 0, [])

    # Print the number of solutions
    print(f"Number of solutions: {len(all_solutions)}")

    for sol in all_solutions:
        print(sol)
