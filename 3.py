import re

def part_one():
    # sample = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)", ''.join(open("3.txt").readlines()))

    res = 0
    for entry in matches:
        res += (int(entry[0]) * int(entry[1]))

    print(res)



def part_two():
    with open("3.txt") as f:
        data = f.read()

    instructions = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", data)

    res, enabled = 0, True  # Default: mul instructions are enabled

    for instruction in instructions:
        if instruction == "don't()":
            enabled = False
        elif instruction == "do()":
            enabled = True
        elif enabled and instruction.startswith("mul"):
            # Extract numbers and compute the product
            x, y = map(int, re.findall(r"\d+", instruction))
            res += x * y

    print(res)

part_two()
