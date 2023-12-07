import string 

d_lower = {chr(i+96):i for i in range(1,27)}
d_upper = {chr(i + 64):(i + 26) for i in range(1, 27)}
score = 0
final_score = 0
x = 0
i = 0
lines = []

with open("day3_2", "r") as file:
    for line in file:
        line.strip()
        length = len(line)
        lines.append(i)
        lines[i] = line
        i = i + 1


for a in range(0,298,3):
    common = set()
    for x in range(0, len(lines[a])):
       for y in range(0, len(lines[a + 1])):
        if (lines[a][x] == lines[a + 1][y]):
            if (lines[a][x] != '\n'):
                common.add(lines[a][x])
        elements = set(lines[a + 2])
        inter = common.intersection(elements)

    for c in inter:
        if c.islower() == True:
            score = score + d_lower.get(c)
        else:
            score = score + d_upper.get(c)
    
    final_score = final_score + score

    score = 0
    common.clear()
    inter.clear()
    elements.clear()

print(final_score)

