from functools import cache

towels, tarr, designs = set(), [], []

with open("19.txt") as file:
    tarr = [ch.strip() for ch in file.readline().strip().split(',')]
    towels = set(tarr)
    file.readline()

    designs = [line.strip() for line in file.readlines()]

# part one
def is_possible(design, c, n):
    if design in n:
        return False

    if design in c:
        return True

    if design in towels:
        c.add(design)
        return True

    for i in range(1, len(design)):
        if is_possible(design[:i], c, n) and is_possible(design[i:], c, n):
            c.add(design)
            return True

    n.add(design)
    return False

res = 0
for d in designs:
    if is_possible(d, set(), set()):
        res += 1

print(res)

@cache
def dfs(design, i):
    if i >= len(design):
        return 1

    res = 0
    for t in towels:
        if len(t) > len(design):
            continue

        if design[i: i + len(t)] == t:
            res += dfs(design, i + len(t))

    return res

res = 0
for d in designs:
    res += dfs(d, 0)

print(res)

