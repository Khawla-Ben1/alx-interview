#!/usr/bin/python3
""" Minimum operations """


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """

    if n <= 1:
        return 0
    for operation in range(2, n+1):
        if n % operation == 0:
            return minOperations(int(n/operation)) + operation
    return 0
