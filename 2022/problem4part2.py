x = 0
y = 0

with open("day4input", "r") as file:
    for line in file:
        number_line = line.split('-')
        numbers = number_line[1].split(',')
        first_half = []
        second_half = []
        for i in range(int(number_line[0]), int(numbers[0]) + 1):
            first_half.append(i)
        for j in range(int(numbers[1]), int(number_line[2]) + 1):
            second_half.append(j)
        first_set = set(first_half)
        second_set = set(second_half)
        common = (first_set.intersection(second_set))
        if len(common) == 0:
            y = y + 1
        else:
            x = x + 1
        first_half.clear()
        second_half.clear()
        first_set.clear()
        second_set.clear


print(x)