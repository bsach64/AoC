trees = []
scenic_scores = []

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
    
for i in range(1, 98):
    for j in range(1, 98):
        flag_right = 1
        scenic_right = 0
        for x in range(j + 1, 99):
            if flag_right == 1:
                if trees[i][j] > trees[i][x]:
                    scenic_right = scenic_right + 1
                    flag_right = flag_right * 1
                else:
                    scenic_right = scenic_right + 1
                    flag_right = flag_right * 0
        flag_left = 1
        scenic_left = 0
        for y in range(j - 1, -1, -1):
            if flag_left == 1:
                if trees[i][j] > trees[i][y]:
                    scenic_left = scenic_left + 1
                    flag_left = flag_left * 1
                else:
                    scenic_left = scenic_left + 1
                    flag_left = flag_left * 0
        flag_top = 1
        scenic_top = 0
        for z in range(i - 1, -1, -1):
            if flag_top == 1:
                if trees[i][j] > trees[z][j]:
                    scenic_top = scenic_top + 1
                    flag_top = flag_top * 1
                else:
                    scenic_top = scenic_top + 1
                    flag_top = flag_top * 0
        scenic_bottom = 0
        flag_bottom = 1
        for b in range(i + 1, 99):
            if flag_bottom == 1:
                if trees[i][j] > trees[b][j]:
                    flag_bottom = flag_bottom * 1
                    scenic_bottom = scenic_bottom + 1
                else:
                    scenic_bottom = scenic_bottom + 1
                    flag_bottom = flag_bottom * 0
        scenic = scenic_top * scenic_bottom * scenic_left * scenic_right
        scenic_scores.append(scenic)
        scenic = 0

answer = max(scenic_scores)
print(scenic_scores)
print(answer)
