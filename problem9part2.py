import copy

def main():
    knots = [Knot() for i in range(10)]
    explored = []
    with open("sample92.txt") as file:
        commands = file.readlines()
    for command in commands:
        if '\n' in command:
            command = command.replace('\n','')
        direction, steps = command.split(" ")
        steps: int = int(steps)
        for j in range(1, steps + 1):
            print(j)
            for i in range(9, 0, -1):
                knots[i], knots[i - 1] = move(knots[i], knots[i - 1], direction)
                for knot in knots:
                    print(f"({knot})", end=" ")
                print()

class Knot:
    def __init__(self, x = 1, y = 1) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
    
    def position(self):
        return (self.x, self.y)
    
def difference(head, tail):
    return ((head.x - tail.x), (head.y - tail.y))

def move(head, tail, direction):
    new_head = copy.deepcopy(head)
    new_tail = copy.deepcopy(tail)
    diff = difference(head, tail)
    if direction == "R":
        if diff == (1, 0):
            new_tail.x += 1
        elif diff == (1, 1):
            new_tail.x += 1
            new_tail.y += 1
        elif diff == (1, -1):
            new_tail.x += 1
            new_tail.y -= 1
        new_head.x += 1
    
    elif direction == "L":
        if diff == (-1, 0):
            new_tail.x -= 1
        elif diff == (-1, 1):
            new_tail.x -= 1
            new_tail.y += 1
        elif diff == (-1, -1):
            new_tail.x -= 1
            new_tail.y -= 1
        new_head.x -= 1
    
    elif direction == "U":
        if diff == (0, 1):
            new_tail.y += 1
        elif diff == (1, 1):
            new_tail.y += 1
            new_tail.x += 1
        elif diff == (-1, 1):
            new_tail.x -= 1
            new_tail.y += 1
        new_head.y += 1

    elif direction == "D":
        if diff == (0, -1):
            new_tail.y -= 1
        elif diff == (-1, -1): 
            new_tail.x -= 1
            new_tail.y -= 1
        elif diff == (1, -1):
            new_tail.x += 1
            new_tail.y -= 1
        new_head.y -= 1
    return new_head, new_tail
    
if __name__ == "__main__":
    main()

