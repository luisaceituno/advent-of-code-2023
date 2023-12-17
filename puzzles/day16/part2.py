from itertools import repeat
from puzzles.day16.common import Tiles, reflections, moves
from utils.coordinates import YX
from utils.read_input import read_input

diagram = read_input()
starting_points: dict[str, list[tuple[int, int]]] = {
    "r": zip(range(0, len(diagram)), repeat(0)),
    "l": zip(range(0, len(diagram)), repeat(len(diagram[0]) - 1)),
    "u": zip(repeat(len(diagram) - 1), range(0, len(diagram[0]))),
    "d": zip(repeat(0), range(0, len(diagram[0]))),
}

optimal = 0
for entry_dir, entry_points in starting_points.items():
    for entry_y, entry_x in entry_points:
        tiles: Tiles = {YX(entry_y, entry_x): [entry_dir]}
        changed: Tiles = tiles.copy()
        while changed:
            coord, beam_dirs = changed.popitem()
            for beam_dir in beam_dirs:
                next_dirs = reflections[coord.on(diagram)][beam_dir]
                for next_dir in next_dirs:
                    next_coord = moves[next_dir](coord)
                    if not next_coord.is_in(diagram):
                        continue
                    tile_dirs = tiles.setdefault(next_coord, [])
                    if next_dir not in tile_dirs:
                        tile_dirs.append(next_dir)
                        changed.setdefault(next_coord, []).append(next_dir)
        optimal = max(optimal, len(tiles))

print(optimal)
