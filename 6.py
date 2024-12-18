sample = '''
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''

def pretty_print(gmap):
    print()
    for row in gmap:
        for entry in row:
            print(entry, end='')
        print()

# gmap = sample.split('\n')
# gmap = gmap[1:len(gmap) - 1]
gmap = open("6.txt").readlines()

gmap = [[ch for ch in line.strip()] for line in gmap]
gpos, sx, sy, didx, directions = set(), 0, 0, 0, [[-1, 0], [0, 1], [1, 0], [0, -1]]

rows, cols = len(gmap), len(gmap[0])
for r in range(rows):
    for c in range(cols):
        if gmap[r][c] == '^':
            sx = r
            sy = c
            break

def part_one(x, y, didx):
    while (
        x in range(rows) and
        y in range(cols)
    ):
        gpos.add((x, y))
        if gmap[x][y] == "." or gmap[x][y] == "X":
            gmap[x][y] = 'X'
            x += directions[didx][0]
            y += directions[didx][1]
        elif gmap[x][y] == "#":
            gpos.remove((x, y))
            x -= directions[didx][0]
            y -= directions[didx][1]
            didx = (didx + 1) % 4
            x += directions[didx][0]
            y += directions[didx][1]

    pretty_print(gmap)
    print("PART ONE", len(gpos))

def cycle(x, y, didx, gmap):
    visited = set()
    while (
        x in range(rows) and
        y in range(cols)
    ):
        if (x, y, didx) in visited: return True
        visited.add((x, y, didx))
        if gmap[x][y] == "." or gmap[x][y] == "^":
            x += directions[didx][0]
            y += directions[didx][1]
        elif gmap[x][y] == "#":
            visited.remove((x, y, didx))
            x -= directions[didx][0]
            y -= directions[didx][1]
            didx = (didx + 1) % 4
            x += directions[didx][0]
            y += directions[didx][1]
    return False


pos = set()
for r in range(rows):
    for c in range(cols):
        if (r, c) != (sx, sy) and gmap[r][c] != "#":
            og = gmap[r][c]
            gmap[r][c] = '#'
            if cycle(sx, sy, didx, gmap):
                pos.add((r, c))
            gmap[r][c] = og

print("PART TWO", len(pos))
part_one(sx, sy, didx)
