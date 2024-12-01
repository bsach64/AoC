one, two = [], []

with open("1.txt") as file:
    line = file.readline()
    while line:
        x, y = map(int, line.split('  '))
        one.append(x)
        two.append(y)
        line = file.readline()


def part_one():
    diffsum = 0
    one.sort()
    two.sort()

    for x, y in zip(one, two):
        diffsum += abs(x - y)

    print(diffsum)

def part_two():
    count, score = dict(), 0
    for y in two:
        count[y] = 1 + count.get(y, 0)

    for x in one:
        if x in count:
            score += x * count[x]

    print(score)

part_one()
part_two()
