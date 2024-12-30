from collections import deque

racetrack = [[ch for ch in line.strip()] for line in open("20.txt").readlines()]

racetrack = [line[1:len(line) - 1] for line in racetrack[1:len(racetrack) - 1]]

start = (0, 0)
rows, cols = len(racetrack), len(racetrack[0])

for r in range(rows):
    for c in range(cols):
        if racetrack[r][c] == 'S':
            start = (r, c)
            break

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

dists = [[-1] * cols for _ in range(rows)]
dists[start[0]][start[1]] = 0

q = deque([start])
while q:
    x, y = q.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (
            nx in range(rows) and
            ny in range(cols) and
            racetrack[nx][ny] != '#' and
            dists[nx][ny] == -1
        ):
            dists[nx][ny] = 1 + dists[x][y]
            q.append((nx, ny))


cnt = 0
for r in range(rows):
    for c in range(cols):
        if dists[r][c] != -1:
            for dx, dy in directions:
                if (
                    r + 2*dx in range(rows) and
                    c + 2*dy in range(cols) and
                    dists[r + 2*dx][c + 2*dy] - dists[r][c] >= 102
                ):
                    cnt += 1
print(f"part one: {cnt}")


def cheat(r, c):
    q = deque([(r, c, 0)])
    cnt = 0
    visited = set()
    while q:
        x, y, t = q.popleft()
        if (x, y) in visited:
            continue

        if dists[x][y] > -1 and dists[x][y] - dists[r][c] >= (100 + t):
            cnt += 1

        visited.add((x, y))
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if (
                nx in range(rows) and
                ny in range(cols) and
                (nx, ny) not in visited and
                t + 1 <= 20
            ):
                q.append((nx, ny, t + 1))

    return cnt


cnt = 0
for r in range(rows):
    for c in range(cols):
        if dists[r][c] != -1:
            cnt += cheat(r, c)

print(f"part two: {cnt}")
