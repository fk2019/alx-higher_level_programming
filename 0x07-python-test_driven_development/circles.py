from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("radius must a non-negative real number")
    if r < 0:
        raise ValueError("radius must be a positive number")
    return pi * (r ** 2)

