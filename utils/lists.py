from functools import reduce
from itertools import cycle
from typing import Callable, Iterable


def multiply(*nums: int):
    return reduce(lambda n, acc: n * acc, nums, 1)


def split_by[T](items: list[T], splitter: Callable[[T], bool]):
    group = []
    for item in items:
        if splitter(item):
            yield group
            group = []
        else:
            group.append(item)
    if group:
        yield group


def diff_elems[T](list_a: list[T], list_b: list[T]):
    for a, b in zip(list_a, list_b):
        if a != b:
            yield (a, b)


def enumerate_2d[T](lines: list[list[T]]):
    """Yields (element, y, x) for each element in the matrix"""
    for y in range(0, len(lines)):
        line = lines[y]
        for x in range(0, len(line)):
            yield line[x], y, x


def filter_2d[T](lines: list[list[T]], predicate: Callable[[T], bool]):
    """Yields (element, y, x) for each element in the matrix that satisfies the predicate"""
    for entry in enumerate_2d(lines):
        if predicate(entry[0]):
            yield entry


def cycle_n[T](iterable: Iterable[T], n: int):
    """Yields n elements from iterable, cycling back to the start once it's exhausted"""
    c = cycle(iterable)
    for i in range(0, n):
        yield next(c)
