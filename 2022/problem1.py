with open("input", "r") as file:
    x = 0
    calories = [0]
    for line in file:
        line.strip()
        string = line
        if line in ['\n', '\r\n']:
            y = 0
            calories.append(y)
            x = x + 1
        else: 
            z = int(string)
            calories[x] = calories[x] + z

calories.sort(reverse = True)

sum = 0
for i in range(0,3):
    print(f"{calories[i]}")
    sum = sum + calories[i]

print(f"{sum}")