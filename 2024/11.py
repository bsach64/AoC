from functools import cache

stones = list(map(int, open("11.txt").readline().strip().split(' ')))

# brute force
def part_one(stones):
    for _ in range(25):
        res = []
        for stone in stones:
            if stone == 0:
                res.append(1)
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                res.append(int(stone_str[:len(stone_str) // 2]))
                res.append(int(stone_str[len(stone_str) // 2:]))
            else:
                res.append(stone * 2024)
        stones = res

    print(len(stones))

@cache
def count_stones(stones, cnt):
    if cnt == 75:
        return len(stones)

    if len(stones) == 1:
        if stones[0] == 0:
            return count_stones(tuple([1]), cnt + 1)

        stone_str = str(stones[0])
        if len(stone_str) % 2 != 0:
            return count_stones(tuple([stones[0] * 2024]), cnt + 1)

        return count_stones(
            (int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])),
            cnt + 1
        )

    res = 0
    for stone in stones:
        res += count_stones(tuple([stone]), cnt)
    return res

print(count_stones(tuple(stones), 0))

