from functools import reduce


def multiply(*nums: int):
    return reduce(lambda n, acc: n * acc, nums, 1)
