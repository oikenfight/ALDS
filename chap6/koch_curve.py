import math


def koch(d, p1x, p1y, p2x, p2y):
    if d == 0:
        return

    sx = (2 * p1x + 1 * p2x) / 3
    sy = (2 * p1y + 1 * p2y) / 3
    tx = (1 * p1x + 2 * p2x) / 3
    ty = (1 * p1y + 2 * p2y) / 3

    # ux = (tx-sx)*math.cos(math.pi/3) - (ty-sy)*math.sin(math.pi/3) + sx
    # uy = (tx-sx)*math.sin(math.pi/3) + (ty-sy)*math.cos(math.pi/3) + sy



    return

if __name__ == '__main__':
    p1x, p1y = 0, 0
    p1x, p1y = 100, 0

    n = int(input())
    koch(n, p1x, p1y, p2x, p2y)