def main():
    rope = Rope()
    explored = []
    with open("input9.txt") as file:
        commands = file.readlines()
    for command in commands:
        if '\n' in command:
            command = command.replace('\n','')
        direction, steps = command.split(" ")
        steps: int = int(steps)
        for _ in range(steps):
            rope.move(direction)
            tail = rope.pos_tail()
            if tail not in explored:
                explored.append(tail)
    print(len(explored))

class Rope:
    def __init__(self) -> None:
        self.hx = 1
        self.hy = 1
        self.tx = 1
        self.ty = 1

    def __str__(self) -> str:
        return f"({self.hx} , {self.hy}), ({self.tx} , {self.ty})"
    def difference(self):
        return ((self.hx - self.tx), (self.hy - self.ty))

    def move(self, direction):
        if direction == "R":
            # no_tail = [(0,0),(0,1),(0,-1),(-1,1),(-1,-1),(-1,0)]
            if self.difference() == (1, 0):
                self.tx += 1
            elif self.difference() == (1, 1): 
                self.tx += 1
                self.ty += 1
            elif self.difference() == (1, -1):
                self.tx += 1
                self.ty -= 1
            self.hx += 1
        elif direction == "L":
            # no_tail  = [(0, 0), (1, 0), (1, 1), (1, -1),(0,1),(0,-1)]
            if self.difference() == (-1, 0):
                self.tx -= 1
            elif self.difference() == (-1, 1):
                self.tx -= 1
                self.ty += 1
            elif self.difference() == (-1, -1):
                self.tx -= 1
                self.ty -= 1
            self.hx -= 1
            
        elif direction == "U":
            # no_tail = [(0,0), (1,0), (-1,0),(0,-1),(-1,-1),(1,-1)]
            if self.difference() == (0, 1):
                self.ty += 1
            elif self.difference() == (1, 1):
                self.ty += 1
                self.tx += 1
            elif self.difference() == (-1, 1):
                self.tx -= 1
                self.ty += 1
            self.hy += 1

        elif direction == "D":
            # no_tail = [(0, 0), (1, 0), (-1, 0), (0, 1),(1,1), (-1, 1)]
            if self.difference() == (0, -1):
                self.ty -= 1
            elif self.difference() == (-1, -1): 
                self.tx -= 1
                self.ty -= 1
            elif self.difference() == (1, -1):
                self.tx += 1
                self.ty -= 1
            self.hy -= 1

    def pos_tail(self):
        return (self.tx, self.ty)
    
if __name__ == "__main__":
    main()

