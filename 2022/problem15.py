import re
import sys

def main():
    # I did not come up with this approach
    sensors, beacons = parse_input("input15.txt")

    positive_coeff: set[int] = set()
    negative_coeff: set[int] = set()

    for i, sensor in enumerate(sensors):
        radius: int = distance(sensor, beacons[i])
        positive_coeff.add(sensor[1] - sensor[0] + radius + 1)
        positive_coeff.add(sensor[1] - sensor[0] - radius - 1)
        negative_coeff.add(sensor[1] + sensor[0] - radius - 1)
        negative_coeff.add(sensor[1] + sensor[0] + radius + 1)

    bound: int = 4_000_000
    for a in positive_coeff:
        for b in negative_coeff:
            p = ((b - a) // 2, (a + b) // 2)
            if all(0 < c < bound for c in p):
                if all(distance(p, s) > distance(s, beacons[i]) for i, s in enumerate(sensors)):
                    print(bound * p[0] + p[1])

def distance(sensor: tuple[int, int], point: tuple[int, int]) -> int:
    return abs(sensor[0] - point[0]) + abs(sensor[1] - point[1])

def parse_input(filename: str) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    sensors: list[tuple[int, int]] = []
    closest_beacon: list[tuple[int, int]] = []

    with open("input15.txt") as file:
        lines = file.readlines()

    pattern = r"Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)\n"

    for line in lines:
        match = re.search(pattern, line)
        if not match:
            sys.exit("Could not find pattern")
        sensors.append((int(match.group(1)), int(match.group(2))))
        closest_beacon.append((int(match.group(3)), int(match.group(4))))
    return sensors, closest_beacon

if __name__ == "__main__":
    main()
