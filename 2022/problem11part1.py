import re

class Monkey:
    def __init__(self) -> None:
        self.number = None
        self.items = []
        self.operation = tuple()
        self.test = 0
        self.actions = dict()
        self.inspect_count = 0

    def create(self, note: list):
        self.number = int(re.search(r"Monkey ([0-9]):",note[0]).group(1))
        self.items = [int(num) for num in re.findall(r"\d+", note[1])]
        operations = re.search(r"(\+|\*) ([0-9]+|old)", note[2][22:])
        self.operation = (operations.group(1), operations.group(2))
        self.test = int(re.search(r"  Test: divisible by ([0-9]+)", note[3]).group(1))
        self.actions['true'] = int(re.findall(r"\d+", note[4])[0])
        self.actions['false'] = int(re.findall(r"\d+", note[5])[0])

def main():
    with open("input11.txt") as file:
        data = file.readlines()

    data = [line.replace('\n','') for line in data]
    notes = [[]]
    i = j = 0
    while i != len(data):
        if data[i] != '':
            notes[j].append(data[i])
            i += 1
        else:
            notes.append([])
            i += 1
            j += 1

    monkeys = []
    for note in notes:
        temp = Monkey()
        temp.create(note)
        monkeys.append(temp)

    for _ in range(20):
        monkeys = simulate_round(monkeys)
    
    counts = []
    for monkey in monkeys:
        counts.append(monkey.inspect_count)
    counts.sort(reverse=True)
    print(counts[0]*counts[1])

def operate(operation, x):
    if operation[0] == "*":
        if operation[1] == "old":
            return (x * x) // 3
        else:
            return (x * int(operation[1])) // 3
    else:
        if operation[1] == "old":
            return (x + x) // 3
        else:
            return (x + int(operation[1])) // 3

def simulate_round(monkeys): 
    for i in range(len(monkeys)):
        while len(monkeys[i].items) > 0:
            monkeys[i].items[0] = operate(monkeys[i].operation, monkeys[i].items[0])
            thing = monkeys[i].items.pop(0)
            if thing % monkeys[i].test == 0:
                monkeys[monkeys[i].actions['true']].items.append(thing)
            else:
                monkeys[monkeys[i].actions['false']].items.append(thing)
            monkeys[i].inspect_count += 1   
    return monkeys

if __name__ == "__main__":
    main()