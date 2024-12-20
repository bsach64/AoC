disk_map = open("9.txt").readline().strip()
# disk_map = "2333133121414131402"

cur_id = 0
file_blocks = []
files = []

for i, sn in enumerate(disk_map):
    n = int(sn)
    if i % 2 == 0:
        file_blocks.extend([str(cur_id)] * n)
        files.append([cur_id, n])
        cur_id += 1
    else:
        file_blocks.extend(['.'] * n)
        files.append([-1, n])

def find_first_dot(file_blocks):
    for i, n in enumerate(file_blocks):
        if n == '.':
            return i
    return -1

def find_last_num(file_blocks):
    for i in range(len(file_blocks) - 1, -1, -1):
        if file_blocks[i] != '.':
            return i
    return -1

def part_one(file_blocks):
    while find_last_num(file_blocks) > find_first_dot(file_blocks):
        dot_idx = find_first_dot(file_blocks)
        last_num_idx = find_last_num(file_blocks)
        file_blocks[dot_idx] = file_blocks[last_num_idx]
        file_blocks[last_num_idx] = '.'

    res, idx = 0, 0
    while file_blocks[idx] != '.':
        res += (idx * int(file_blocks[idx]))
        idx += 1

    print(res)

# part_one(file_blocks)
i = len(files) - 1
done = set()

def pretty_print(files):
    res = []
    for f in files:
        if f[0] == -1:
            res.append('.' * f[1])
        else:
            res.append(str(f[0]) * f[1])

    print(''.join(res))

while i > 0 and len(done) < cur_id:
    if i in done:
        i -= 1
        continue
    if files[i][0] == -1:
        i -= 1
        continue
    for j in range(len(files)):
        if files[j][0] != -1:
            continue
        if j > i:
            break
        if files[j][1] >= files[i][1]:
            files[j][1] -= files[i][1]
            done.add(files[i][0])
            to_move = files[i].copy()
            files[i][0] = -1
            files = files[:j] + [to_move] + files[j:]
            break
    i -= 1

res, cnt = 0, 0
for f in files:
    if f[0] == -1:
        cnt += f[1]
        continue
    for _ in range(f[1]):
        res += (f[0] * cnt)
        cnt += 1
print(res)

