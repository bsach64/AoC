amap = [[ch for ch in line.strip()] for line in open("8.txt").readlines()]
unique = dict()

def pretty_print(amap):
    for row in amap:
        for ch in row:
            print(ch, end='')
        print()

for i, row in enumerate(amap):
    for j, ch in enumerate(row):
        if ch == '.':
            continue
        if ch not in unique:
            unique[ch] = []
        unique[ch].append((i, j))


rows = len(amap)
cols = len(amap[0])

def part_one():
    visited = set()
    antinode = set()
    for ch in unique:
        for one in unique[ch]:
            for two in unique[ch]:
                if one == two:
                    continue
                if (one, two) in visited or (two, one) in visited:
                    continue
                visited.add((one, two))
                dist = abs(one[0] - two[0])
                # slope
                m = (two[1] - one[1]) / (two[0] - one[0])
                # point one
                x = one[0] - dist
                y = (m * (x - one[0])) + one[1]
                if x >= 0 and y >= 0 and x < rows and y < cols:
                    amap[int(x)][int(y)] = '#'
                    antinode.add((int(x), int(y)))
                # point two
                x = two[0] + dist
                y = (m * (x - one[0])) + one[1]
                if x >= 0 and y >= 0 and x < rows and y < cols:
                    amap[int(x)][int(y)] = '#'
                    antinode.add((int(x), int(y)))

    pretty_print(amap)
    print(len(antinode))

def part_two():
    visited = set()
    antinode = set()
    for ch in unique:
        for one in unique[ch]:
            for two in unique[ch]:
                if one == two:
                    continue
                if (one, two) in visited or (two, one) in visited:
                    continue
                visited.add((one, two))
                dist = abs(one[0] - two[0])
                # slope
                m = (two[1] - one[1]) / (two[0] - one[0])
                x = one[0] - dist
                y = (m * (x - one[0])) + one[1]
                while x >= 0 and y >= 0 and x < rows and y < cols:
                    amap[int(x)][int(y)] = '#'
                    antinode.add((int(x), int(y)))
                    x = x - dist
                    y = (m * (x - one[0])) + one[1]

                x = two[0] + dist
                y = (m * (x - one[0])) + one[1]
                while x >= 0 and y >= 0 and x < rows and y < cols:
                    amap[int(x)][int(y)] = '#'
                    antinode.add((int(x), int(y)))
                    x = x + dist
                    y = (m * (x - one[0])) + one[1]

    for ch in unique:
        if len(unique[ch]) > 1:
            antinode = antinode.union(unique[ch])

    pretty_print(amap)
    print(len(antinode))

part_two()

