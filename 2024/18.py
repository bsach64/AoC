from heapq import heappop, heappush
from collections import deque

space = [['.' for _ in range(71)] for _ in range(71)]

with open("18.txt") as file:
    corrupted = file.readlines()

def pretty_print(space):
    for row in space:
        for ch in row:
            print(ch, end='')
        print()

def man_distance(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1])

rows, cols = len(space), len(space[0])
start, end = (0, 0), (70, 70)
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def count_steps():
    visited = set()
    h = [(0, *start)]
    while h:
        s, x, y = heappop(h)

        if (x, y) == end:
            return s

        if (x, y) in visited: continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                nx in range(rows) and
                ny in range(cols) and
                space[nx][ny] != '#' and
                (nx, ny) not in visited
            ):
                heappush(h, (s + 1, nx, ny))

    return -1

for i, cor in enumerate(corrupted):
    x, y = cor.strip().split(',')
    space[int(y)][int(x)] = '#'
    if i > 1024 and count_steps() == -1:
        print(x, y)
        break
