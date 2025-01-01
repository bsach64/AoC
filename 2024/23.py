connections = dict()

with open("23.txt") as file:

    lines = file.readlines()

    for l in lines:
        x, y = l.strip().split('-')

        if x not in connections:
            connections[x] = set()
        if y not in connections:
            connections[y] = set()

        connections[x].add(y)
        connections[y].add(x)


def part_one():
    three_tuples = set()

    for one in connections:
        for two in connections[one]:
            for three in connections[two]:
                if (
                    one in connections[two] and
                    two in connections[three] and
                    three in connections[one] and (
                        one[0] == "t" or two[0] == "t" or three[0] == "t"
                    )
                ):
                    three_tuples.add(frozenset([one, two, three]))

    print(len(three_tuples))

max_clique = set()
for start in connections:
    clique = {start}
    for v in connections:
        connected = True
        for c in clique:
            if v not in connections[c]:
                connected = False
                break

        if connected:
            clique.add(v)

    if len(clique) > len(max_clique):
        max_clique = clique.copy()

print(len(max_clique))
l = list(max_clique)
l.sort()
print(','.join(l))
