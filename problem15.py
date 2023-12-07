import re


min_x = -2
min_y = 0


def main():
    region = [['.' for _ in range(31)] for _ in range(23)]

    with open("sample15.txt") as file:
        lines = file.readlines()

    pattern = r"Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)\n"

    for line in lines:
        match = re.search(pattern, line)
        sensor = (int(match.group(1)) - min_x, int(match.group(2)) - min_y)
        beacon = (int(match.group(3)) - min_x, int(match.group(4)) - min_y)
        region[sensor[1]][sensor[0]] = 'S'
        region[beacon[1]][beacon[0]] = 'B'
        mark_no_beacon(region, sensor, beacon)

    print_map(region)


def print_map(region):
    for row in region:
        for entry in row:
            print(entry, end='')
        print()


def mark_no_beacon(region, sensor, beacon, y=10):
    m_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    print(sensor, beacon, m_distance)
    for i in range(31):
        distance = abs(sensor[0] - i) + abs(sensor[1] - 10)
        if distance == m_distance:
            if region[10][sensor[0] - i] != 'S' and region[10][sensor[0] - i] != 'B':
                region[10][sensor[0] - i] = '#'


if __name__ == "__main__":
    main()
