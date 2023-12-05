from itertools import chain

from puzzles.day05.common import parse_almanac
from utils.read_input import read_input

lines = read_input()
almanac = parse_almanac(lines)

seed_ranges = almanac.seed_ranges()


def partition_range(range1: range, range2: range):
    start1, end1 = range1.start, range1.stop
    start2, end2 = range2.start, range2.stop
    break_points: list[int] = []
    [
        break_points.append(point)
        for point in sorted([start1, end1, start2, end2])
        if point >= start1 and point <= end1 and point not in break_points
    ]
    ranges: list[range] = []
    for i in range(len(break_points) - 2 + 1):
        s, e = break_points[i : i + 2]
        ranges.append(range(s, e))
    return ranges


cur_ranges = seed_ranges
for a_map in almanac.maps:
    for a_range in a_map.ranges:
        cur_ranges = list(
            chain.from_iterable(
                map(
                    lambda r: partition_range(
                        r, range(a_range.source, a_range.source + a_range.count)
                    ),
                    cur_ranges,
                )
            )
        )
    cur_ranges = list(
        map(lambda r: range(a_map.map(r.start), a_map.map(r.stop - 1)), cur_ranges)
    )

print(min(cur_ranges, key=lambda r: r.start).start)
