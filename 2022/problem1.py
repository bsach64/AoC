with open("input1.txt", "r") as file:
    calories = [0]
    for line in file:
        if line == '\n':
            calories.append(0)
        else:
            calories[-1] = calories[-1] + int(line)

calories.sort(reverse=True)

sum = calories[0] + calories[1] + calories[2]
print(sum)
