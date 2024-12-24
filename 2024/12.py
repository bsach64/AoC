from collections import deque

garden = [[ch for ch in line.strip()] for line in open("12.txt").readlines()]

rows = len(garden)
cols = len(garden[0])

unique_gardens = []
visited = set()
directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def bfs(r, c):
    plant = garden[r][c]
    garden_plot = set()

    q = deque()
    q.append((r, c))
    garden_plot.add((r, c))

    while q:
        r, c = q.popleft()

        for dx, dy in directions:
            if (
                r + dx in range(rows) and
                c + dy in range(cols) and
                (r + dx, c + dy) not in garden_plot and
                garden[r + dx][c + dy] == plant
            ):
                q.append((r + dx, c + dy))
                garden_plot.add((r + dx, c + dy))

    return garden_plot

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            garden_plot = bfs(r, c)
            visited = visited.union(garden_plot)
            unique_gardens.append(garden_plot)

def part_one(unique_gardens):
    res = 0
    for garden in unique_gardens:
        perimeter = 0
        for node in garden:
            pnode = 4
            for dx, dy in directions:
                if (node[0] + dx, node[1] + dy) in garden:
                    pnode -= 1
            perimeter += pnode
        res += (perimeter * len(garden))

    print(res)

def corner_count(x, y, garden):
    cnt = 0
    if (x - 1, y - 1) not in garden:
        if (x - 1, y) in garden and (x, y - 1) in garden:
            cnt += 1

        if (x - 1, y) not in garden and (x, y - 1) not in garden:
            cnt += 1

    if (x + 1, y + 1) not in garden:
        if (x + 1, y) in garden and (x, y + 1) in garden:
            cnt += 1
        if (x + 1, y) not in garden and (x, y + 1) not in garden:
            cnt += 1

    if (x - 1, y + 1) not in garden:
        if (x - 1, y) in garden and (x, y + 1) in garden:
            cnt += 1
        if (x - 1, y) not in garden and (x, y + 1) not in garden:
            cnt += 1

    if (x + 1, y - 1) not in garden:
        if (x + 1, y) in garden and (x, y - 1) in garden:
            cnt += 1
        if (x + 1, y) not in garden and (x, y - 1) not in garden:
            cnt += 1

    if (x - 1, y - 1) in garden and (x - 1, y) not in garden and (x, y - 1) not in garden:
        cnt += 1

    if (x + 1, y + 1) in garden and (x + 1, y) not in garden and (x, y + 1) not in garden:
        cnt += 1

    if (x - 1, y + 1) in garden and (x - 1, y) not in garden and (x, y + 1) not in garden:
        cnt += 1

    if (x + 1, y - 1) in garden and (x + 1, y) not in garden and (x, y - 1) not in garden:
        cnt += 1

    return cnt

def part_two(unique_gardens):
    res = 0
    for garden in unique_gardens:
        corners = 0
        for x, y in garden:
            corners += corner_count(x, y, garden)
        print(corners)
        res += (len(garden) * corners)

    print(res)
part_two(unique_gardens)
