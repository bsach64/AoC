with open("inputday6", "r") as file:
    for line in file:
        length = len(line)
        for i in range(0, length):
            characters = line[i : i + 14]
            characters_set = set(characters)
            if len(characters_set) == 14:
                print(i + 14)
                break