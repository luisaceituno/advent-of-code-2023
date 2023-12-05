from collections import deque
from dataclasses import dataclass


@dataclass
class AlmanacRange:
    source: int
    target: int
    count: int

    def map(self, source_num: int):
        diff = source_num - self.source
        if diff >= 0 and diff < self.count:
            return self.target + diff


@dataclass
class AlmanacMap:
    type_from: str
    type_to: str
    ranges: list[AlmanacRange]

    def map(self, source_num: int):
        return next(
            (
                target
                for target in map(lambda r: r.map(source_num), self.ranges)
                if target != None
            ),
            source_num,
        )


@dataclass
class Almanac:
    seeds: list[int]
    maps: list[AlmanacMap]

    def map_for_src(self, source: str):
        return next(mapping for mapping in self.maps if mapping.type_from == source)

    def find_for_seed(self, seed: int, type: str):
        cur_type = "seed"
        cur_val = seed
        while cur_type != type:
            mapping = self.map_for_src(cur_type)
            cur_type = mapping.type_to
            cur_val = mapping.map(cur_val)
        return cur_val

    def seed_ranges(self):
        return [
            range(seed, seed + self.seeds[idx + 1])
            for idx, seed in enumerate(self.seeds)
            if idx % 2 == 0
        ]


def parse_almanac(lines: list[str]):
    next = deque(lines)
    seeds = [int(seed) for seed in next.popleft().replace("seeds: ", "").split(" ")]
    almanac = Almanac(seeds, [])
    while next:
        next.popleft()
        [type_from, type_to] = (
            next.popleft().replace("-to-", "-").replace(" map:", "").split("-")
        )
        mapping = AlmanacMap(type_from, type_to, [])
        almanac.maps.append(mapping)
        while next and next[0]:
            target, source, count = (
                int(num_str) for num_str in next.popleft().split(" ")
            )
            mapping.ranges.append(AlmanacRange(source, target, count))
    return almanac
