#!/usr/bin/python3
"""Nqueens algorithm in python"""
import sys


def backtrack(r, n, columns, pos, neg, board):
    """_summary_

    Args:
        r (_type_): _description_
        n (_type_): _description_
        columns (_type_): _description_
        pos (_type_): _description_
        neg (_type_): _description_
        board (_type_): _description_
    """
    if r == n:
        res = []
        for i in range(len(board)):
            for k in range(len(board[i])):
                if board[i][k] == 1:
                    res.append([i, k])
        print(res)
        return

    for c in range(n):

        if c in columns or (r + c) in pos or (r - c) in neg:
            continue

        columns.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, columns, pos, neg, board)

        columns.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """_summary_

    Args:
        n (_type_): _description_
    Return:
         List of lists repres coordinates for each queens
    """
    columns = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, columns, pos_diag, neg_diag, board)


if __name__ == '__main__':
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(n[1])
        if N < 4:
            print("N must Be at least 4")
            sys.exit(1)
        nqueens(N)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
