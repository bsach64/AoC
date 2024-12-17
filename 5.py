text = [line.strip() for line in open("5.txt").readlines()]
text = text[1:len(text) - 1]
read_order = False
before, after = dict(), dict()
updates = []

for line in text:
    if line == "":
        read_order = True
        continue

    if not read_order:
        x, y = map(int, line.split('|'))
        if y in before:
            before[y].append(x)
        else:
            before[y] = [x]

        if x in after:
            after[x].append(y)
        else:
            after[x] = [y]
        continue

    updates.append(list(map(int, [x for x in line.split(',') if x.strip()])))

def check_page(page):
    idx_map, rel = dict(), set(page)
    for i, entry in enumerate(page):
        idx_map[entry] = i

    for i, entry in enumerate(page):
        if entry in before:
            for bef in before[entry]:
                if bef not in rel:
                    continue
                if idx_map[bef] > i:
                    return False

        if entry in after:
            for af in after[entry]:
                if af not in rel:
                    continue
                if idx_map[af] < i:
                    return False

    return True

one, two = 0, 0
for page in updates:
    if check_page(page):
        one += page[len(page) // 2]

print("PART ONE", one)
