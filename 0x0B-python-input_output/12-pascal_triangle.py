"""Module deines pascals triangle
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing pascals
    triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        end = triangle[-1]
        tmp = [1]
        for i in range(len(end) - 1):
            tmp.append(end[i] + end[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
