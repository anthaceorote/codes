''' 
Given 4 points, determine if they form a square 

Logic: A quadrilateral is a square if all its sides are equal and its diagonals are equal
'''


from math import sqrt
from itertools import combinations
from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


class Edge:
    def __init__(self, p1, p2):
        self.start = p1
        self.end = p2
        self.dist()

    def dist(self):
        self.cost = sqrt((self.start.x - self.end.x)**2 + (self.start.y - self.end.y)**2)

    def __repr__(self):
        return "Edge({}, {}) = {}".format(self.start, self.end, self.cost)


def is_square(pts):
    sides = [Edge(p1, p2) for p1, p2 in combinations(pts, 2)]
    sides = sorted(sides, key=lambda x: x.cost)
    sqr_side_len, diag_len = sides[0].cost, sides[-1].cost
    if not (diag_len > sqr_side_len):
        return False
    for side in sides[1:4]:
        if side.cost != sqr_side_len:
            return False
    if sides[-2].cost != sides[-1].cost:
        return False
    return True


def print_pts(pts):
    max_x = max(abs(pt.x) for pt in pts)
    max_y = max(abs(pt.y) for pt in pts)
    grid = [[0] * (max_y + 2) for _ in range(max_x + 2)]

    for pt in pts:
        grid[pt.x][pt.y] = 1

    for row in grid:
        for val in row:
            print('X' if val else '.', end='')
        print()


def main():
    pts = [(0, 0), (0, 1), (1, 0), (1, 1)]
    max_len = 10
    pts = [(randint(0, max_len), randint(0, max_len)) for _ in range(4)]
    pts = [Point(*p) for p in pts]
    while not is_square(pts):
        pts = [(randint(0, max_len), randint(0, max_len)) for _ in range(4)]
        pts = [Point(*p) for p in pts]
    print(pts)
    print_pts(pts)


if __name__ == '__main__':
    main()
