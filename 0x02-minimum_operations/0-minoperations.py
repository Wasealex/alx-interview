#!/usr/bin/python3
"""
module containing minOperations function that calculates
the fewest number of operations needed to result in exactly
n 'H' characters in the file
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to result in exactly
    n 'H' characters in the file
    """
    if n <= 1:
        return 0
    # prime factorization
    operations = 0
    divisor = 2
    while n > 1:
        # if n is divisible by divisor, divide n by divisor
        # and add divisor to operations
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            # if n is not divisible by divisor, increment divisor by 1
            divisor += 1
            # if divisor is greater than n, break
            if divisor > n:
                break
    return operations
