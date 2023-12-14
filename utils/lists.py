from functools import reduce
from typing import Callable


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
