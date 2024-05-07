#!/usr/bin/python3
"""Method that calculates the fewest number of operations needed to result in
exactly n H characters in the file"""


def minOperations(n):
    """Calculates the fewest number """
    if n ==1:
        return 0

    operations = 0
    clipboard = 1
    count = 1

    while count < n:
        if n % count ==0:
            operations += 2
            clipboard = count 
            count *= 2
        else:
            operations +=1
            count += clipboard

    return operations