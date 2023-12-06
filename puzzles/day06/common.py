from decimal import Decimal
import numpy


def max_uncertainty(n: float):
    """Round number after five decimal places to avoid some unwanted uncertainty"""
    return Decimal(n).quantize(Decimal("1.00000"))


def press_min_max(time: int, distance: int):
    """Solve quadratic equation "distance = (time - x) * x" where x is the time we press the button"""
    root1, root2 = sorted(numpy.roots([1, -time, distance]))
    root1, root2 = max_uncertainty(root1), max_uncertainty(root2)
    return numpy.floor(root1) + 1, numpy.ceil(root2) - 1
