from collections import deque

topo = [[int(ch) for ch in line.strip()] for line in open("10.txt").readlines()]

rows = len(topo)
cols = len(topo[0])
cnt = 0

def bfs(x, y):
    nines = set()

    q = deque()
    q.append((x, y, 0, []))
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    while q:
        x, y, cur, path = q.popleft()
        for dx, dy in directions:
            if (
                x + dx in range(rows) and
                y + dy in range(cols) and
                topo[x + dx][y + dy] == cur + 1
            ):
                q.append((x + dx, y + dy, cur + 1, path + [x + dx, y + dy]))
                if cur + 1 == 9:
                    nines.add((x + dx, y + dy, tuple(path)))
    return len(nines)

res = 0
for r in range(rows):
    for c in range(cols):
        if topo[r][c] == 0:
            res += bfs(r, c)

print(res)

