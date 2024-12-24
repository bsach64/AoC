lines = [line.strip() for line in open("13.txt").readlines()]
prizes, prize = [], []
for i, line in enumerate(lines):
    if i % 4 == 0 or i % 4 == 1:
        x, y = line.split(':')[1].split(',')
        x, y = int(x.split('+')[1]), int(y.split('+')[1])
        prize.append([x, y])
    elif i % 4 == 2:
        x, y = line.split(':')[1].split(',')
        x, y = int(x.split('=')[1]), int(y.split('=')[1])
        prize.append([x, y])
    else:
        prizes.append(prize.copy())
        prize = []

prizes.append(prize)
# brute force just for fun

def brute(p):
    for a in range(101):
        for b in range(101):
            x = a * p[0][0] + b * p[1][0]
            y = a * p[0][1] + b * p[1][1]
            if x == p[2][0] and y == p[2][1]:
                return a, b
    return 0, 0

def part_one():
    res = 0
    for p in prizes:
        a, b = brute(p)
        res += (3 * a + b)

    print(res)

# linear equation solving
def part_two():
    res = 0
    for _, p in enumerate(prizes):
        c1, c2 = 10000000000000 + p[2][0], 10000000000000 + p[2][1]
        # c1, c2 =  p[2][0], p[2][1]
        x1, y1 = p[0][0], p[1][0]
        x2, y2 = p[0][1], p[1][1]
        d = ((x1 * y2) - (x2 * y1))
        a = ((y2 * c1) - (y1 * c2)) / d
        b = ((-x2 * c1) + (x1 * c2)) / d
        if a.is_integer() and b.is_integer():
            res += (3 * a + b)

    print(res)

part_one()
part_two()
