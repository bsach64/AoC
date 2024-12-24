text = open("15.txt").readlines()

grid, movements, m_started = [], "", False

for line in text:
    if line == '\n':
        m_started = True
        continue

    if not m_started:
        grid.append([ch for ch in line.strip()])
    else:
        movements += ''.join(line.strip())

def pretty_print(grid):
    for row in grid:
        for c in row:
            print(c, end='')
        print()
    print()


def move_box(robot, bx, by, dx, dy):
    if grid[bx + dx][by + dy] == '.':
        grid[robot[0]][robot[1]] = '.'
        grid[robot[0] + dx][robot[1] + dy] = '@'
        robot[0] += dx
        robot[1] += dy
        grid[bx + dx][by + dy] = 'O'
    elif grid[bx + dx][by + dy] == 'O':
        move_box(robot, bx + dx, by + dy, dx, dy)


def part_one(grid):
    robot, rows, cols = [0, 0], len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                robot = [r, c]

    offset = {'^': (-1, 0), 'v':(1, 0), '>':(0, 1), '<': (0, -1)}
    for m in movements:
        dx, dy = offset[m]

        if (
            robot[0] + dx not in range(rows) or
            robot[1] + dy not in range(cols) or
            grid[robot[0] + dx][robot[1] + dy] == '#'
        ):
            continue

        if grid[robot[0] + dx][robot[1] + dy] == '.':
            grid[robot[0] + dx][robot[1] + dy] = '@'
            grid[robot[0]][robot[1]] = '.'
            robot[0] += dx
            robot[1] += dy

        elif grid[robot[0] + dx][robot[1] + dy] == 'O':
            move_box(robot, robot[0] + dx, robot[1] + dy, dx, dy)

        pretty_print(grid)


    res = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'O':
                res += (r * 100 + c)

    print(res)

# part_one(grid)

def move_big_box(tgrid, robot, bx, by, m):
    offset = {'^': (-1, 0), 'v':(1, 0), '>':(0, 1), '<': (0, -1)}
    dx, dy = offset[m]
    # easier cases first
    if m == '>':
        assert(tgrid[bx][by] == '[')
        assert(tgrid[bx + dx][by + dy] == ']')
        if tgrid[bx + 2 * dx][by + 2 * dy] == '.':
            tgrid[bx + 2 * dx][by + 2 * dy] = ']'
            tgrid[bx + dx][by + dy] = '['
            return True
        elif tgrid[bx + 2 * dx][by + 2 * dy] == '[':
            if move_big_box(tgrid, robot, bx + 2 * dx, by + 2 * dy, m):
                tgrid[bx + 2 * dx][by + 2 * dy] = ']'
                tgrid[bx + dx][by + dy] = '['
                return True
    elif m == '<':
        assert(tgrid[bx][by] == ']')
        assert(tgrid[bx + dx][by + dy] == '[')
        if tgrid[bx + 2 * dx][by + 2 * dy] == '.':
            tgrid[bx + 2 * dx][by + 2 * dy] = '['
            tgrid[bx + dx][by + dy] = ']'
            return True
        elif tgrid[bx + 2 * dx][by + 2 * dy] == ']':
            if move_big_box(tgrid, robot, bx + 2 * dx, by + 2 * dy, m):
                tgrid[bx + 2 * dx][by + 2 * dy] = '['
                tgrid[bx + dx][by + dy] = ']'
                return True

    # moving up
    elif m == '^' or m == 'v':
        if tgrid[bx][by] == ']':
            assert(tgrid[bx][by - 1] == '[')
            if tgrid[bx + dx][by + dy] == '.' and tgrid[bx + dx][by + dy - 1] == '.':
                tgrid[bx + dx][by + dy] = ']'
                tgrid[bx + dx][by + dy - 1] = '['
                tgrid[bx][by] = '.'
                tgrid[bx][by - 1] = '.'
                return True
            elif tgrid[bx + dx][by + dy] == ']' and tgrid[bx + dx][by + dy - 1] == '[':
                if move_big_box(tgrid, robot, bx + dx, by + dy, m):
                    return move_big_box(tgrid, robot, bx, by, m)
            elif tgrid[bx + dx][by + dy] == '[' and tgrid[bx + dx][by + dy - 1] == ']':
                # difficult task
                if move_big_box(tgrid, robot, bx + dx, by + dy, m):
                    if move_big_box(tgrid, robot, bx + dx, by + dy - 1, m):
                        return move_big_box(tgrid, robot, bx, by, m)
                    # revert first box movement
                    tgrid[bx + 2 * dx][by + 2 * dy] = '.'
                    tgrid[bx + (2 * dx)][by + (2 * dy) + 1] = '.'
                    tgrid[bx + dx][by + dy] = '['
                    tgrid[bx + dx][by + dy + 1] = ']'
            elif tgrid[bx + dx][by + dy] == '.' and tgrid[bx + dx][by + dy - 1] == ']':
                if move_big_box(tgrid, robot, bx + dx, by + dy - 1, m):
                    return move_big_box(tgrid, robot, bx, by, m)
            elif tgrid[bx + dx][by + dy] == '[' and tgrid[bx + dx][by + dy - 1] == '.':
                if move_big_box(tgrid, robot, bx + dx, by + dy, m):
                    return move_big_box(tgrid, robot, bx, by, m)
        elif tgrid[bx][by] == '[':
            assert(tgrid[bx][by + 1] == ']')
            if tgrid[bx + dx][by + dy] == '.' and tgrid[bx + dx][by + dy + 1] == '.':
                tgrid[bx + dx][by + dy] = '['
                tgrid[bx + dx][by + dy + 1] = ']'
                tgrid[bx][by] = '.'
                tgrid[bx][by + 1] = '.'
                return True
            elif tgrid[bx + dx][by + dy] == '[' and tgrid[bx + dx][by + dy + 1] == ']':
                if move_big_box(tgrid, robot, bx + dx, by + dy, m):
                    return move_big_box(tgrid, robot, bx, by, m)
            elif tgrid[bx + dx][by + dy] == ']' and tgrid[bx + dx][by + dy + 1] == '[':
                # difficult task
                if move_big_box(tgrid, robot, bx + dx, by + dy - 1, m):
                    if move_big_box(tgrid, robot, bx + dx, by + dy + 1, m):
                        return move_big_box(tgrid, robot, bx, by, m)
                    # revert first box movement
                    tgrid[bx + dx][by + dy] = ']'
                    tgrid[bx + dx][by + dy - 1] = '['
                    tgrid[bx + (2 * dx)][by + (2 * dy)] = '.'
                    tgrid[bx + (2 * dx)][by + (2 * dy) - 1] = '.'
            elif tgrid[bx + dx][by + dy] == ']' and tgrid[bx + dx][by + dy + 1] == '.':
                if move_big_box(tgrid, robot, bx + dx, by + dy - 1, m):
                    return move_big_box(tgrid, robot, bx, by, m)
            elif tgrid[bx + dx][by + dy] == '.' and tgrid[bx + dx][by + dy + 1] == '[':
                if move_big_box(tgrid, robot, bx + dx, by + dy + 1, m):
                    return move_big_box(tgrid, robot, bx, by, m)

        return False

def part_two(grid):
    tgrid = []
    robot, rows, cols = [0, 0], len(grid), len(grid[0])
    offset = {'^': (-1, 0), 'v':(1, 0), '>':(0, 1), '<': (0, -1)}

    for r in range(rows):
        trow = []
        for c in range(cols):
            if grid[r][c] == '#':
                trow.append('#')
                trow.append('#')
            elif grid[r][c] == '.':
                trow.append('.')
                trow.append('.')
            elif grid[r][c] == '@':
                trow.append('@')
                trow.append('.')
            elif grid[r][c] == 'O':
                trow.append('[')
                trow.append(']')
        tgrid.append(trow.copy())

    rows, cols = len(tgrid), len(tgrid[0])

    for r in range(rows):
        for c in range(cols):
            if tgrid[r][c] == '@':
                robot = [r, c]
                break

    for m in movements:
        dx, dy = offset[m]

        if (
            robot[0] + dx not in range(rows) or
            robot[1] + dy not in range(cols) or
            tgrid[robot[0] + dx][robot[1] + dy] == '#'
        ):
            continue

        # print(tgrid[robot[0] + dx][robot[1] + dy])
        if tgrid[robot[0] + dx][robot[1] + dy] == '.':
            tgrid[robot[0] + dx][robot[1] + dy] = '@'
            tgrid[robot[0]][robot[1]] = '.'
            robot[0] += dx
            robot[1] += dy

        elif tgrid[robot[0] + dx][robot[1] + dy] == '[' or tgrid[robot[0] + dx][robot[1] + dy] == ']':
            if move_big_box(tgrid, robot, robot[0] + dx, robot[1] + dy, m):
                tgrid[robot[0] + dx][robot[1] + dy] = '@'
                tgrid[robot[0]][robot[1]] = '.'
                robot[0] += dx
                robot[1] += dy
            else:
                print("Could not move")

        # if i > 4:
        pretty_print(tgrid)
        # break
        # if i == 1:
        #     break

    res = 0
    for r in range(rows):
        for c in range(cols):
            if tgrid[r][c] == '[':
                res += (r * 100 + c)

    print(res)
    # pretty_print(tgrid)

part_two(grid)
