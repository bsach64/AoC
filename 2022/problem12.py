from util import Node, QueueFrontier

def main():
    with open("input12.txt") as file:
        map = file.readlines()

    map = [line.replace('\n','') for line in map]

    starts = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                starts.append((i, j))
            elif map[i][j] == 'a':
                starts.append((i, j))
            elif map[i][j] == 'E':
                target = (i, j)
    paths = []
    for start in starts:
        try:
            paths.append(len(shortest_path(map, start, target)))
        except TypeError:
            pass
    print(min(paths))


def shortest_path(map, source, target):
    frontier = QueueFrontier()
    explored = set()
    start = Node(state=source, parent=None, action=None)
    frontier.add(start)
    while True:
        if frontier.empty():
            return None
        
        current_node = frontier.remove()
        explored.add(current_node.state)

        for move in possible_moves(map, current_node.state):
            if not frontier.contains_state(move) and move not in explored:
                new_node = Node(state=move, parent=current_node, action=None)
                current_path = check_goal(new_node, target)
                if current_path == None:
                    frontier.add(new_node)
                else:
                    return current_path


def check_goal(node, target):
    if node.state == target:
        path = []
        while node.parent is not None:
            path.append(node.state)
            node = node.parent
        path.reverse()
        return path


def possible_moves(map, location):
    elevation = map[location[0]][location[1]]
    if elevation == 'S':
        elevation = 'a'
    possibilities = []
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    for move in moves:
        try:
            x = location[0] + move[0]
            y = location[1] + move[1]
            next = map[x][y]
            if map[x][y] == 'S':
                next = 'a'
            if map[x][y] == 'E':
                next = 'z'
            if x >= 0 and y >= 0:
                try:
                    climbable = ord(next) - ord(elevation)
                    if climbable <= 1:
                        possibilities.append((x,y))
                except IndexError:
                    pass
        except IndexError:
            pass
    return possibilities

if __name__ == "__main__":
    main()
