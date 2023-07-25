import copy

def main():
    with open("input9.txt") as file:
        commands = file.readlines()
    knots = [Knot() for _ in range(10)]
    explored = []
    for command in commands:
        if '\n' in command:
            command = command.replace('\n','')
        direction, steps = command.split(" ")
        steps: int = int(steps)
        for _ in range(steps):
            knots[9] = move_head(knots[9], direction)
            for i in range(8, -1, -1):
                knots[i] = move_tail(knots[i + 1], knots[i])
            tail = knots[0].position()
            if tail not in explored:
                explored.append(tail)
    print(len(explored))        

class Knot:
    def __init__(self, x = 1, y = 1) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def position(self):
        return (self.x, self.y)
    
def difference(head, tail):
    return ((head.x - tail.x), (head.y - tail.y))

def move_head(head, direction):
    new = copy.deepcopy(head)
    if direction == "R":
        new.x += 1
    elif direction == "L":
        new.x -= 1
    elif direction == "U":
        new.y += 1
    elif direction == "D":
        new.y -= 1
    return new

def move_tail(new, tail):
    new_tail = copy.deepcopy(tail)
    diff = difference(new, new_tail)

    if diff == (2,2) or diff == (1,2) or diff == (2, 1):
        new_tail.x += 1
        new_tail.y += 1
    elif diff == (0, 2):
        new_tail.y += 1
    elif diff == (0, -2):
        new_tail.y -= 1
    elif diff == (2, 0):
        new_tail.x += 1
    elif diff == (-2, 0):
        new_tail.x -= 1
    elif diff == (2, -1) or diff == (2, -2) or diff == (1, -2):
        new_tail.x += 1
        new_tail.y -=1 
    elif diff == (-2, -1) or diff == (-2, -2) or diff == (-1, -2):
        new_tail.x -= 1
        new_tail.y -= 1
    elif diff == (-2, 1) or diff == (-2, 2) or diff == (-1, 2):
        new_tail.x -= 1
        new_tail.y += 1

    return new_tail

if __name__ == "__main__":
    main()