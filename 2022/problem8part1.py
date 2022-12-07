trees = []

with open("InputDay8", "r") as file:
    line_counter = 0
    for line in file:
        trees.append([])
        for i in range(0, len(line)):
            if line[i] == '\n':
                pass
            else:
                trees[line_counter].append(int(line[i]))
        line_counter = line_counter + 1
    
print(len(trees))
print(len(trees[0]))

visible_count = 392
visible = 0
for i in range(1, 98):
    for j in range(1, 98):
        flag_right = 1
        for x in range(j + 1, 99):
            if trees[i][j] > trees[i][x]:
                flag_right = flag_right * 1
            else:
                flag_right = flag_right * 0
        if flag_right == 1:
            visible = visible + 1
        flag_left = 1
        for y in range(0, j):
            if trees[i][j] > trees[i][y]:
                flag_left = flag_left * 1
            else:
                flag_left = flag_left * 0
        if flag_left == 1:
            visible = visible + 1
        flag_top = 1
        for z in range(0, i):
            if trees[i][j] > trees[z][j]:
                flag_top = flag_top * 1
            else:
                flag_top = flag_top * 0
        if flag_top == 1:
            visible = visible + 1
        flag_bottom = 1
        for b in range(i + 1, 99):
            if trees[i][j] > trees[b][j]:
                flag_bottom = flag_bottom * 1
            else:
                flag_bottom = flag_bottom * 0
        if flag_bottom == 1:
            visible = visible + 1
        if visible > 0:
            visible_count = visible_count + 1
            visible = 0

print(visible_count)
