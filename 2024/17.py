import math
# Read the input

with open("17.txt") as file:
    a = int(file.readline().strip().split(':')[1])
    b = int(file.readline().strip().split(':')[1])
    c = int(file.readline().strip().split(':')[1])
    file.readline()
    program = list(map(int, file.readline().strip().split(':')[1].strip().split(',')))


def comb_input(inp):
    if inp >= 0 and inp < 4:
        # print(f' {inp}')
        return inp
    if inp == 4:
        # print(f' a={a}')
        return a
    if inp == 5:
        # print(f' b={b}')
        return b
    if inp == 6:
        # print(f' c={c}')
        return c
    return -1

ip, b, c = 0, 0, 0
while ip < len(program):
    opcode = program[ip]
    inp = program[ip + 1]

    if opcode == 0: # adv
        # print("0 adv", end='')
        a = int(a / math.pow(2, comb_input(inp)))
        # print(f"new value of a={a}")

    elif opcode == 1:
        # print(f"1 bxl {inp}")
        b = (b ^ inp)
        # print(f"new value of b={b}")

    elif opcode == 2:
        # print("2 bst", end='')
        b = comb_input(inp) % 8
        # print(f"new value of b={b}")

    elif opcode == 3:
        # print(f"3 jnz a={a}")
        if a != 0:
            # print(f"new value of ip={ip}")
            ip = inp
            continue

    elif opcode == 4:
        # print(f"4 bxc")
        b = (b ^ c)
        # print(f"new value of b={b}")
    elif opcode == 5:
        # print("5 out", end='')
        val = comb_input(inp) % 8
        print(f"outputed val={val}")
    elif opcode == 6:
        b = int(a / math.pow(2, comb_input(inp)))
    elif opcode == 7:
        # print("7 cdv", end='')
        c = int(a / math.pow(2, comb_input(inp)))
        # print(f"new value of c={c}")
    ip += 2


def part_two(program):
    # input specific

    def find(program, ans):
        if not program: return ans
        for b in range(8):
            a = (ans << 3) + b
            b = b ^ 7
            c = a >> b
            b = b ^ c
            b = b ^ 7
            if (b % 8) == program[-1]:
                sub = find(program[:-1], a)
                if sub is not None: return sub

    print(program, find(program, 0))

part_two(program)
