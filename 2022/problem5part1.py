import re

crates = []

for i in range(0, 9):
    crates.append([])

with open("inputday5", "r") as file:
    line_count = 0
    for line in file:
        if line_count < 8:
            line_count = line_count + 1
            x = 0
            for i in range(1, len(line), 4):
                if line[i] == " ":
                    x = x + 1
                else:
                    crates[x].append(line[i])
                    x = x + 1

        if re.match("^move", line):
            x = re.findall('[0-9]+', line)
            num_crates = int(x[0])
            initial_crate = int(x[1])
            final_crate = int(x[2])
            for i in range(0, num_crates):
                x = crates[initial_crate - 1][0]
                crates[final_crate - 1].insert(0, x)
                crates[initial_crate - 1].pop(0)

for i in range(0, 9):   
    print(crates[i][0], end ="")

print()

