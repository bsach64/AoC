import re

def main():    
    with open("input14.txt") as file:
        data = file.readlines()

    paths = []
    cave = [['.' for _ in range(200)] for _ in range(200)]
    for path in data:
        match = re.findall('([0-9]+),([0-9]+) *-*>*',path)
        paths.append([(int(entry[1]),int(entry[0]) - 494) for entry in match])
    for path in paths:
        for i in range(1,len(path)):
            cave = draw_rock(path[i - 1], path[i], cave)
    cave[0][6] = '+'
    sands = 0
    while True:
        try:
            move_down, move_x = drop_sand(cave)
            cave[move_down][6 + move_x] = 'o'
            sands += 1
        except TypeError:
            break
    print(sands)

def draw_rock(p_one, p_two, cave):
    if p_one[0] == p_two[0]:
        line = sorted([p_one[1], p_two[1]])
        for i in range(line[0], line[1] + 1):
            cave[p_one[0]][i] = '#'
    elif p_one[1] == p_two[1]:
        line = sorted([p_one[0], p_two[0]])
        for i in range(line[0], line[1] + 1):
            cave[i][p_one[1]] = '#'
    return cave

def drop_sand(cave, move_down = -1):
    start = 6 
    move_x = 0
    try:
        while True:
            if cave[move_down + 1][start] == '.' or cave[move_down + 1][start] == '+':
                move_down += 1
            elif cave[move_down + 1][start] == 'o':
                while True:
                    if cave[move_down + 1][start + move_x] == '.':
                        move_down += 1
                    elif cave[move_down + 1][start + move_x - 1] == '.':
                        move_x += -1
                        move_down += 1
                    elif cave[move_down + 1][start + move_x + 1] == '.':
                        move_x += 1
                        move_down += 1
                    else:
                        break
                break
            else:
                break
        return move_down, move_x
    except IndexError:
        return None

if __name__ == "__main__":
    main()