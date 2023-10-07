import string

d_lower = {chr(i+96):i for i in range(1,27)}
d_upper = {chr(i + 64):(i + 26) for i in range(1, 27)}
score = 0


with open("day3_2", "r") as file:
    for line in file:
        line.strip()
        length = len(line)
        length = length - 1
        chunks = int(length / 2)
        first_half = [line[i: i + chunks] for i in range(0,chunks, chunks)]
        second_half = [line[i: i + chunks] for i in range(chunks, length, chunks)]
        common = set()
        for x in range(0, chunks):
            for y in range(0, chunks):
                if (first_half[0][x] == second_half[0][y]):
                    if first_half[0][x].islower() == True:
                        common.add(first_half[0][x])
                    else:
                        common.add(first_half[0][x])
        for i in common:
            if i.islower() == True:
                score = score + d_lower.get(i)
            else:
                score = score + d_upper.get(i)


print(score)


