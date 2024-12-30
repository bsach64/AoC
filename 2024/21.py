from heapq import heappush, heappop
from functools import cache

codes = [line.strip() for line in open("21.txt").readlines()]

numpad = [['.'] * 3 for _ in range(4)]

keypad = [['.'] * 3 for _ in range(2)]

numpad[0][0] = '7'
numpad[0][1] = '8'
numpad[0][2] = '9'
numpad[1][0] = '4'
numpad[1][1] = '5'
numpad[1][2] = '6'
numpad[2][0] = '1'
numpad[2][1] = '2'
numpad[2][2] = '3'
numpad[3][0] = '.'
numpad[3][1] = '0'
numpad[3][2] = 'A'

keypad[0][1] = '^'
keypad[0][2] = 'A'
keypad[1][0] = '<'
keypad[1][1] = 'v'
keypad[1][2] = '>'

nrows, ncols = len(numpad), len(numpad[0])
directions = [[-1, 0, "^"], [1, 0, "v"], [0, 1, ">"], [0, -1, "<"]]

def all_paths(start, end, pad):
    if start == end:
        return set([""])
    rows, cols = len(pad), len(pad[0])
    h, lowest, shortest_paths = [(0, *start, "")], float('inf'), set()

    while h:
        s, x, y, path = heappop(h)

        if (x, y) == end:
            if s > lowest: return shortest_paths

            lowest = s
            shortest_paths.add(path)

        for dx, dy, m in directions:
            nx, ny = x + dx, y + dy
            if (
                nx in range(rows) and
                ny in range(cols) and
                pad[nx][ny] != '.'
            ):
                heappush(h, (s + 1, nx, ny, path + m))

key_paths = dict()
for sr in range(2):
    for sc in range(3):
        for er in range(2):
            for ec in range(3):
                if keypad[sr][sc] != '.' and keypad[er][ec] != '.':
                    key_paths[(keypad[sr][sc], keypad[er][ec])] = all_paths((sr, sc), (er, ec), keypad)


num_paths = dict()
for sr in range(4):
    for sc in range(3):
        for er in range(4):
            for ec in range(3):
                if numpad[sr][sc] != '.' and numpad[er][ec] != '.':
                    num_paths[(numpad[sr][sc], numpad[er][ec])] = all_paths((sr, sc), (er, ec), numpad)



def all_nums_to_keys(code):
    res = []
    res = []
    def np_to_kp(c, seq, i):
        if i == len(c):
            res.append(seq)
            return

        prev = 'A'
        if i > 0:
            prev = c[i - 1]

        paths = num_paths[(prev, c[i])]
        for p in paths:
            np_to_kp(c, seq + p + 'A', i + 1)

    np_to_kp(code, "", 0)
    return res


def all_seqs(keys):
    res = []
    def kp_to_kp(c, seq, i):
        if i == len(c):
            res.append(seq)
            return

        prev = 'A'
        if i > 0:
            prev = c[i - 1]

        paths = key_paths[(prev, c[i])]
        for p in paths:
            kp_to_kp(c, seq + p + 'A', i + 1)

    kp_to_kp(keys, "", 0)
    return res

def shortest_seq(keys, depth, c):
    if depth == 0:
        return len(keys)

    if (keys, depth) in c:
        return c[(keys, depth)]

    # split the keys into subkeys at current depth
    sub_keys, prev = [], 0
    for i in range(len(keys)):
        if keys[i] != 'A': continue

        sub_keys.append(keys[prev: i + 1])
        prev = i + 1

    res = 0

    for sk in sub_keys:
        # find all ways to build sub key at depth - 1
        all_seqs_for_sk = all_seqs(sk)
        cur_min = float('inf')
        for sq in all_seqs_for_sk:
            cur_min = min(cur_min, shortest_seq(sq, depth - 1, c))
        res += cur_min

    c[(keys, depth)] = res
    return res

final = 0
for c in codes:
    res = float('inf')
    keys = all_nums_to_keys(c)
    for k in keys:
        res = min(res, shortest_seq(k, 25, dict()))

    final += (res * int(c[:len(c) - 1]))

print(final)
