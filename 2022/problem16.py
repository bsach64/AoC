import re
from math import inf
from copy import deepcopy


def main():
    with open('sample16.txt') as file:
        lines = file.readlines()

    valves = establish_map(lines)
    valves_to_visit = find_valves_to_visit(valves)
    minutes = 30
    flowrate = 0
    last_valve = None
    current_valve = valves['AA']

    while minutes > 0 and len(valves_to_visit) != 0:
        distances = find_distance(valves, current_valve)
        next_valve = best_next_valve_v2(valves, current_valve, valves_to_visit, last_valve, minutes)
        print(next_valve.name, end=' ')
        if should_open(valves, next_valve.name, valves_to_visit, minutes):
            minutes -= (distances[next_valve.name] - 1)
            flowrate += minutes * next_valve.flowrate
            try:
                valves_to_visit.remove(next_valve.name)
            except ValueError:
                pass
        print(valves_to_visit)
        current_valve = next_valve
    print(flowrate)


class Valve:
    def __init__(self, name, flowrate=0):
        self.name = name
        self.flowrate = flowrate
        self.tunnels = set()

    def __str__(self):
        return str(self.flowrate) + str({tunnel.name: tunnel.flowrate for tunnel in self.tunnels})


def establish_tunnels(valves: dict, valve: Valve, tunnels: str):
    tunnels = [tunnel.strip() for tunnel in tunnels.split(',')]
    for tunnel in tunnels:
        if tunnel in valves:
            valves[tunnel].tunnels.add(valve)
        else:
            new_tunnel = Valve(name=tunnel)
            new_tunnel.tunnels.add(valve)
            valves[valve.name].tunnels.add(new_tunnel)
            valves[tunnel] = new_tunnel


def find_distance(valves: dict, starting_valve: Valve):
    distances = dict()
    explored = set()
    for valve in valves:
        if valve == starting_valve.name:
            distances[valve] = 0
        else:
            distances[valve] = inf

    current_valve = starting_valve
    frontier = list(current_valve.tunnels)
    while len(explored) != len(valves):
        for tunnel in current_valve.tunnels:
            if distances[tunnel.name] == inf:
                distances[tunnel.name] = distances[current_valve.name] + 1
            elif distances[tunnel.name] > distances[current_valve.name] + 1:
                distances[tunnel.name] = distances[current_valve.name] + 1
            if tunnel not in frontier and tunnel not in explored:
                frontier.append(tunnel)
        explored.add(current_valve)
        if frontier:
            current_valve = frontier.pop()

    return distances


def find_path(valves, starting_valve, ending_valve):
    path = []
    distances = dict()
    explored = set()
    for valve in valves:
        new_node = Node(valve)
        if valve == starting_valve.name:
            new_node.distance = 0
        else:
            new_node.distance = inf
        distances[valve] = new_node

    current_valve = starting_valve
    frontier = list(current_valve.tunnels)
    while True:
        for tunnel in current_valve.tunnels:
            if distances[tunnel.name].distance == inf:
                distances[tunnel.name].distance = distances[current_valve.name].distance + 1
                distances[tunnel.name].parent = current_valve.name
            elif distances[tunnel.name].distance > distances[current_valve.name].distance + 1:
                distances[tunnel.name].distance = distances[current_valve.name].distance + 1
                distances[tunnel.name].parent = current_valve.name
            if tunnel not in frontier and tunnel not in explored:
                frontier.append(tunnel)
        explored.add(current_valve)
        if current_valve == ending_valve:
            break
        if frontier:
            current_valve = frontier.pop()
    traveller = ending_valve.name
    path.append(traveller)
    while traveller != starting_valve.name:
        traveller = distances[traveller].parent
        path.append(traveller)

    return path


def establish_map(lines):
    pattern = r"Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnel(?:s)? lead(?:s)? to valve(?:s)? ((?:[A-Z]{2},? ?)+)\n"

    valves = dict()

    for line in lines:
        match = re.search(pattern, line)
        if match.group(1) in valves:
            valves[match.group(1)].flowrate = int(match.group(2))
            establish_tunnels(valves, valves[match.group(1)], match.group(3))
        else:
            new_valve = Valve(name=match.group(1), flowrate=int(match.group(2)))
            valves[match.group(1)] = new_valve
            establish_tunnels(valves, new_valve, match.group(3))
    return valves


def find_valves_to_visit(valves):
    valves_to_visit = []
    for valve in valves:
        if valves[valve].flowrate > 0:
            valves_to_visit.append(valve)
    return valves_to_visit


def score_valve(valves, current_valve, valves_to_visit, minutes):
    temp_list = deepcopy(valves_to_visit)
    minutes_copy = deepcopy(minutes)
    distances = find_distance(valves, current_valve)
    score = 0
    for entry in distances:
        if entry in valves_to_visit:
            if should_open(valves, entry, valves_to_visit, minutes):
    
    return score


def best_next_valve_v2(valves, current_valve, valves_to_visit, last_valve, minutes):
    max_score = 0
    next_valve = None
    if len(current_valve.tunnels) == 1:
        return list(current_valve.tunnels)[0]
    for tunnel in current_valve.tunnels:
        valve_score = score_valve(valves, tunnel, valves_to_visit, minutes - 1)
        if valve_score > max_score and tunnel != last_valve:
            next_valve = tunnel
            max_score = valve_score
    return next_valve


class Node:
    def __init__(self, name, parent=None, distance=0):
        self.name = name
        self.parent = parent
        self.distance = distance


def should_open(valves, current_valve, valves_to_visit, minutes):
    distances = find_distance(valves, valves[current_valve])
    reduced_minutes = minutes - 2
    opened_flowrate = valves[current_valve].flowrate * reduced_minutes
    closed_flowrate = 0
    for entry in distances:
        if entry in valves_to_visit and entry != current_valve:
            opened_flowrate += valves[entry].flowrate * (reduced_minutes - distances[entry] - 1)
            closed_flowrate += valves[entry].flowrate * (minutes - distances[entry] - 1)
    return opened_flowrate > closed_flowrate


if __name__ == "__main__":
    main()
