import sys


def read_input():
    return [line.removesuffix("\n") for line in sys.stdin]
