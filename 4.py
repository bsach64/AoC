text = [line for line in open("4.txt").readlines() if line.strip()]
cnt = 0

def check_word(row, col):
    if text[row][col] != "A":
        return False

    try:
        if (
            text[row - 1][col - 1] == "M" and text[row + 1][col + 1] == "S" or
            text[row - 1][col - 1] == "S" and text[row + 1][col + 1] == "M"
        ):
            if (
                text[row - 1][col + 1] == "M" and text[row + 1][col - 1] == "S" or
                text[row - 1][col + 1] == "S" and text[row + 1][col - 1] == "M"
            ):
                return True

    except IndexError:
        return False
    return False

for row in range(len(text)):
    for col in range(len(text[0])):
        if check_word(row, col):
            cnt += 1

print(cnt)
