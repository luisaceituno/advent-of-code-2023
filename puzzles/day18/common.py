from utils.coordinates import YX


def blocky_shoelace(corners: list[YX]):
    area = 0
    border = 0
    for i in range(len(corners)):
        (y1, x1) = corners[i]
        (y2, x2) = corners[(i + 1) % len(corners)]
        area += (x1 * y2) - (x2 * y1)
        border += abs(x2 - x1 + y2 - y1)
    return int(abs(area / 2) + border / 2 + 1)
