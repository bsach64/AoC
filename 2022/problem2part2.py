# A ROCK  1
# B PAPER  2
# C SCISSORS  3
# X loss = 0
# Y draw = 3
# Z win = 6


with open("day2", "r") as file:
    score = 0
    for line in file:
        line.strip()
        if line[2] == 'X':
            if line[0] == 'A':
                score = score + 3
            elif line[0] == 'B':
                score = score + 1
            elif line[0] == 'C':
                score = score + 2
        elif line[2] == 'Y':
            score = score + 3
            if line[0] == 'A':
                score = score + 1
            elif line[0] == 'B':
                score = score + 2
            elif line[0] == 'C':
                score = score + 3
        elif line[2] == 'Z':
            score = score + 6
            if line[0] == 'A':
                score = score + 2
            elif line[0] == 'B':
                score = score + 3
            elif line[0] == 'C':
                score = score + 1


print(f"{score}")
