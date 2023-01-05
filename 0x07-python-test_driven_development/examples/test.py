"""This module defines a factorial function"""

import math

def factorial(n):
    """returns factorial of n
    Args:
        n: First parameter
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise TypeError("n must be a number")
    if n + 1 == n:
        raise OverflowError("n is too large")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
