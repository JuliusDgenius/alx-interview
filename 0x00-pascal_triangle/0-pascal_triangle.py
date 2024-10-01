#!/usr/bin/python3
"""
that returns a list of lists of integers representing
the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer
"""
from math import factorial


def pascal_triangle(n):
    """Returns pascal triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)

    return triangle

    # return [[factorial(i) // (factorial(j)
    #          * factorial(i - j)) for j in range(i + 1)] for i in range(n)]
