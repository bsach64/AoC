nums = list(map(int, [line.strip() for line in open("22.txt").readlines()]))

def next_secret_num(n):
    ns = n << 6
    n = ns ^ n
    n = n % 16777216
    ns = n >> 5
    n = ns ^ n
    n = n % 16777216
    ns = n << 11
    n = ns ^ n
    n = n % 16777216
    return n

def get_data(n):
    prices, diffs = [int(str(n)[-1])], []

    ns = n
    for _ in range(2000):
        ns = next_secret_num(ns)
        prices.append(int(str(ns)[-1]))
        diffs.append(prices[-1] - prices[-2])

    return prices, diffs

seq_map = dict()
for i, n in enumerate(nums):
    prices, diffs = get_data(n)
    for j in range(3, len(diffs)):
        seq = (diffs[j - 3], diffs[j - 2], diffs[j - 1], diffs[j])
        if seq not in seq_map:
            seq_map[seq] = [0] * len(nums)
            seq_map[seq][i] = prices[j + 1]
        else:
            if seq_map[seq][i] == 0:
                seq_map[seq][i] = prices[j + 1]

max_key = None
max_bana = 0
for k in seq_map:
    ss = sum(seq_map[k])
    if ss > max_bana:
        max_bana = ss
        max_key = k

print(max_bana, max_key, seq_map[max_key])
