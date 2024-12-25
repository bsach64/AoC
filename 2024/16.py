from heapq import heappush, heappop

maze = [list(line.strip()) for line in open("16.txt")]
rows, cols = len(maze), len(maze[0])

start, end = [0, 0], [0, 0]
for r in range(rows):
    for c in range(cols):
        if maze[r][c] == 'S':
            start = (r, c)
        elif maze[r][c] == 'E':
            end = (r, c)

h = [(0, start[0], start[1], 0, 1, [])]
tiles = set()
lowest_score = float('inf')
best_cost = {(*start, 0, 1): 0}

while h:
    score, r, c, dr, dc, path = heappop(h)
    if score > best_cost.get((r, c, dr, dc), float('inf')): continue
    best_cost[(r, c, dr, dc)] = score

    if maze[r][c] == 'E':
        if score > lowest_score: break

        lowest_score = score
        for p in path:
            tiles.add((p[0], p[1]))

    for new_score, nr, nc, ndr, ndc in [(score + 1, r + dr, c + dc, dr, dc), (score + 1000, r, c, dc, -dr), (score + 1000, r, c, -dc, dr)]:
        if maze[nr][nc] == "#": continue
        if new_score > best_cost.get((nr, nc, ndr, ndc), float('inf')): continue
        best_cost[(nr, nc, ndr, ndc)] = new_score
        heappush(h, (new_score, nr, nc, ndr, ndc, path + [(nr, nc, ndr, ndc)]))

print(tiles)
print(lowest_score)
print(len(tiles))
