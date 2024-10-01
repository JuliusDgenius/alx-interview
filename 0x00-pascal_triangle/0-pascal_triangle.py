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
    return [[factorial(i) // (factorial(j)
             * factorial(i - j)) for j in range(i + 1)] for i in range(n)]
