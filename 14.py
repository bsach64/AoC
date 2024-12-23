robots = [line.strip().split(' ') for line in open("14.txt").readlines()]
robots = [list(map(int, [line[0][2:].split(',')[0], line[0][2:].split(',')[1], line[1][2:].split(',')[0], line[1][2:].split(',')[1]])) for line in robots]

from PIL import Image


def grid_to_image(grid, i):
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    img = Image.new('L', (width, height))

    for y in range(height):
        for x in range(width):
            color = 255 if grid[y][x] == '1' else 0  # White for '1', Black for '.'
            img.putpixel((x, y), color)

    filename = f"{i}.jpg"
    img.save(filename)

def part_one(robots):
    for robot in robots:
        robot[0] = (robot[0] + 100 * robot[2]) % 101
        robot[1] = (robot[1] + 100 * robot[3]) % 103

    quad = [0, 0, 0, 0]
    for robot in robots:
        x, y = robot[0], robot[1]
        if x < 50 and y < 51:
            quad[0] += 1
        elif x < 50 and y > 51:
            quad[1] += 1
        elif x > 50 and y > 51:
            quad[2] += 1
        elif x > 50 and y < 51:
            quad[3] += 1

    print(quad[0] * quad[1] * quad[2] * quad[3])

bathroom = [['.'] * 101 for _ in range(103)]

min_dst, min_bathroom = float('inf'), []
for i in range(10000):

    for j in range(len(bathroom)):
        for k in range(len(bathroom[0])):
            bathroom[j][k] = '.'
    dist = 0
    for n, robot in enumerate(robots):
        robot[0] = (robot[0] + robot[2]) % 101
        robot[1] = (robot[1] + robot[3]) % 103
        bathroom[robot[1]][robot[0]] = '1'

    # see images generated for ans
    grid_to_image(bathroom, i)
