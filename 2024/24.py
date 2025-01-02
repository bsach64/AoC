from heapq import heappop, heappush

wires = dict()
dependency = dict()
gates = dict()
inverse_gate = dict()

with open("24.txt") as file:
    line = file.readline()
    while line != '\n':
        name, val = line.strip().split(':')
        name = name.strip()
        val = int(val.strip())
        wires[name] = val
        dependency[name] = set()
        line = file.readline()

    line = file.readline()
    while line:
        exp, out = line.strip().split('->')
        left, op, right = exp.strip().split(' ')
        out = out.strip()
        gates[out] = [left, op, right]
        inverse_gate[(left, op, right)] = out
        if out not in dependency:
            dependency[out] = set()
        dependency[out].add(left)
        dependency[out].add(right)
        line = file.readline()


def part_one():
    order, visit = [], set()

    # topological sort
    def dfs(wire):
        if wire in visit:
            return

        for depend in dependency[wire]:
            dfs(depend)

        visit.add(wire)
        order.append(wire)

        dependency[wire] = set()

    for wire in dependency.copy():
        dfs(wire)

    for wire in order:
        if wire in wires: continue

        left, op, right = gates[wire]

        if op == 'AND':
            wires[wire] = wires[left] & wires[right]
        elif op == 'OR':
            wires[wire] = wires[left] | wires[right]
        elif op == 'XOR':
            wires[wire] = wires[left] ^ wires[right]

    h = []
    for wire in wires:
        if wire[0] != 'z': continue

        idx = int(wire[1:])
        heappush(h, (-idx, wires[wire]))

    res = ""

    while h:
        _, val = heappop(h)
        res += str(val)

    print(int(res, 2))


assert('z00' == inverse_gate[('y00', 'XOR', 'x00')])

carry = inverse_gate[('y00', 'AND', 'x00')]

x, y = 1, 1

'''
y01 XOR x01 -> hqt
hfm XOR hqt -> z01
'''
for i in range(1, 45):
    xstr = 'x' + str(i)
    if i < 10:
        xstr = 'x0' + str(i)

    ystr = 'y' + str(i)
    if i < 10:
        ystr = 'y0' + str(i)

    zstr = 'z' + str(i)
    if i < 10:
        zstr = 'z0' + str(i)

    # sum = A (XOR) B (XOR) Carry (zi)
    sum_val = None
    if (xstr, 'XOR', ystr) in inverse_gate:
        sum_val = inverse_gate[(xstr, 'XOR', ystr)]
    elif (ystr, 'XOR', xstr) in inverse_gate:
        sum_val = inverse_gate[(ystr, 'XOR', xstr)]

    if not sum_val:
        print(f"HERE expected: {(xstr, 'XOR', ystr)}")
        break

    # calculate zi == sum
    if (carry, 'XOR', sum_val) in inverse_gate:
        if inverse_gate[(carry, 'XOR', sum_val)] != zstr:
            print(f"expected: {(carry, 'XOR', sum_val), zstr, xstr, ystr}")
            break
    elif (sum_val, 'XOR', carry) in inverse_gate:
        if inverse_gate[(sum_val, 'XOR', carry)] != zstr:
            print(f"expected: {(carry, 'XOR', sum_val), zstr, xstr, ystr}")
            break
    else:
        print(f"expected sum: {(carry, 'XOR', sum_val), carry, xstr}")
        break

    # calculate new carry
    # Carry = (A (AND) B) OR (carry (AND) sum_val)
    xay = None
    if (xstr, 'AND', ystr) in inverse_gate:
        xay = inverse_gate[(xstr, 'AND', ystr)]
    elif (ystr, 'AND', xstr) in inverse_gate:
        xay = inverse_gate[(ystr, 'AND', xstr)]

    if not xay:
        print(f"expected: {(xstr, 'AND', ystr)}")
        break

    carry_and_sum = None
    if (carry, 'AND', sum_val) in inverse_gate:
        carry_and_sum = inverse_gate[(carry, 'AND', sum_val)]
    elif (sum_val, 'AND', carry) in inverse_gate:
        carry_and_sum = inverse_gate[(sum_val, 'AND', carry)]

    if not carry_and_sum:
        print(f"expected: {(carry, 'AND', sum_val)}")
        break

    carry = None
    if (xay, 'OR', carry_and_sum) in inverse_gate:
        carry = inverse_gate[(xay, 'OR', carry_and_sum)]
    elif (carry_and_sum, 'OR', xay) in inverse_gate:
        carry = inverse_gate[(carry_and_sum, 'OR', xay)]

    if not carry_and_sum:
        print(f"expected: {(carry_and_sum, 'OR', xay)}")
        break

    x += 1
    y += 1
