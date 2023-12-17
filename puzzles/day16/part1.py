from puzzles.day16.common import Tiles, moves, reflections
from utils.coordinates import YX
from utils.read_input import read_input

diagram = read_input()
tiles: Tiles = {YX(0, 0): ["r"]}
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

print(len(tiles))
