#!/usr/bin/python3
"""Task 12. Pascal's Triangle"""


def pascal_triangle(n):
    '''
        Returns a list of lists of ints representing the Pascal’s triangle of n

        Args:
            n: An integer, the number of rows of the triangle.

        Returns:
            A list of lists representing Pascal's Triangle.
    '''
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(i + 1):
                if j > 0 and j < i:
                    row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
