from utils.coordinates import YX

reflections = {
    ".": {"u": ["u"], "r": ["r"], "d": ["d"], "l": ["l"]},
    "\\": {"u": ["l"], "r": ["d"], "d": ["r"], "l": ["u"]},
    "/": {"u": ["r"], "r": ["u"], "d": ["l"], "l": ["d"]},
    "-": {"u": ["l", "r"], "r": ["r"], "d": ["l", "r"], "l": ["l"]},
    "|": {"u": ["u"], "r": ["u", "d"], "d": ["d"], "l": ["u", "d"]},
}
Dir = str  # u, r, d, l
Tiles = dict[YX, list[Dir]]
moves = {"u": YX.up, "r": YX.right, "d": YX.down, "l": YX.left}
