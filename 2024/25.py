locks, keys = set(), set()
lines = []

with open("25.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def parse_grid(grid):
    heights = [0 for _ in range(5)]

    for row in grid:
        for i, ch in enumerate(row):
            if ch == '#':
                heights[i] += 1

    return heights

i = 0
while i < len(lines):
    if lines[i] == '#####':
        heights = parse_grid(lines[i + 1: i + 6])
        i += 8
        locks.add(tuple(heights))
    elif lines[i] == '.....':
        heights = parse_grid(lines[i + 1: i + 6])
        i += 8
        keys.add(tuple(heights))

print(locks)
print(keys)

res = 0

for lock in locks:
    for key in keys:
        fits = True
        for i in range(5):
            if key[i] + lock[i] > 5:
                fits = False
                break

        if fits: res += 1

print(res)
