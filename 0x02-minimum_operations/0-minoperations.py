#!/usr/bin/python3
"""
Defines a method that returns the least number of operations
required to give exactly n out of H character in a file.
"""


def minOperations(n):
    """
    Returns the least  number of operations needed to result in exactly
    n H characters in the file.
    """
    operations = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            operations += min_ops
            n /= min_ops
        min_ops += 1
    return operations
