import sys
import re
from dataclasses import dataclass
import heapq
from collections import deque

@dataclass
class Valve:
    flowrate: int
    neighbours: set[str]

@dataclass
class State:
    curr: str
    opened: set[str]
    elapsed: int
    relieved: int

def parse(filename: str) -> dict[str, Valve]:
    with open(filename) as file:
        lines: list[str] = file.readlines()

    pattern: str = r"Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnel(?:s)? lead(?:s)? to valve(?:s)? ((?:[A-Z]{2},? ?)+)\n"
    valves: dict[str, Valve] = dict()

    for line in lines:
        match: re.Match[str] | None = re.search(pattern, line)
        if not match:
            sys.exit(1)
        name: str = match.group(1)
        flowrate: int = int(match.group(2))
        tunnels: list[str] = match.group(3).split(',')
        tunnels = [t.strip() for t in tunnels]
        valves[name] = Valve(flowrate, set(tunnels))

    return valves

def distance(start: str, end: str, valves: dict[str, Valve]) -> int:
    pq: list[tuple[int, str]] = []
    seen: set[str] = set()

    heapq.heappush(pq, (0, start))
    seen.add(start)

    while pq:
        entry: tuple[int, str] = heapq.heappop(pq)
        if entry[1] == end:
            return entry[0]

        for n in valves[entry[1]].neighbours:
            if n not in seen:
                heapq.heappush(pq, (entry[0] + 1, n))
                seen.add(n)

    return int('inf')

def calc_min_distances(valves: dict[str, Valve]) -> dict[tuple[str, str], int]:
    min_dist:  dict[tuple[str, str], int] = dict()
    min_dist[("AA", "AA")] = 0
    for val in valves:
        if valves[val].flowrate > 0:
            min_dist[("AA", val)] = distance("AA", val, valves)
    for start in valves:
        if valves[start].flowrate > 0:
            for end in valves:
                if valves[end].flowrate > 0:
                    min_dist[(start, end)] = distance(start, end, valves)
    return min_dist

def wait_until_ending(max_time: int, elapsed, relieved, opened, valves):
    time_left = max_time - elapsed
    for v in opened:
        relieved += (valves[v].flowrate * time_left)
    return relieved

def part_one() -> int:
    valves: dict[str, Valve] = parse("input16.txt")
    min_distances: dict[tuple[str, str], int] = calc_min_distances(valves)
    flowing: set[str] = set([v for v in valves if valves[v].flowrate > 0])
    max_relieved: int = 0
    dq = deque([State("AA", set(), 0, 0)])
    seen: set[tuple[frozenset[str], int, int]] = set((frozenset(), 0, 0))

    while dq:
        state: State = dq.popleft()

        if len(state.opened) == len(flowing) or state.elapsed >= 30:
            relieved_at_end = wait_until_ending(30, state.elapsed, state.relieved, state.opened, valves)
            max_relieved = max(relieved_at_end, max_relieved)
            continue

        unopened = flowing - state.opened
        for v in unopened:
            cost: int = min_distances[(state.curr, v)] + 1
            new_elapsed = state.elapsed + cost
            if new_elapsed >= 30:
                relieved_at_end = wait_until_ending(30, state.elapsed, state.relieved, state.opened, valves)
                max_relieved = max(relieved_at_end, max_relieved)
                continue

            relieved_per_min = 0
            for vopen in state.opened:
                relieved_per_min += valves[vopen].flowrate

            new_opened = state.opened.copy()
            new_opened.add(v)
            new_relieved = state.relieved + (relieved_per_min * cost)
            new_state = State(v, new_opened, new_elapsed, new_relieved)
            state_info = (frozenset(new_opened), new_elapsed, new_relieved)
            if state_info not in seen:
                dq.append(new_state)
                seen.add(state_info)
    return max_relieved


def part_two() -> int:
    valves: dict[str, Valve] = parse("input16.txt")
    min_distances: dict[tuple[str, str], int] = calc_min_distances(valves)
    flowing: set[str] = set([v for v in valves if valves[v].flowrate > 0])
    max_relieved_states: dict[frozenset[str], int] = set()
    dq = deque([State("AA", set(), 0, 0)])
    seen: set[tuple[frozenset[str], int, int]] = set((frozenset(), 0, 0))

    while dq:
        state: State = dq.popleft()

        relieved_at_end = wait_until_ending(26, state.elapsed, state.relieved, state.opened, valves)
        fopened = frozenset(state.opened)
        if fopened not in max_relieved_states:
            max_relieved_states[fopened] = relieved_at_end
        else:
            max_relieved_states[fopened] = max(relieved_at_end, max_relieved_states[fopened])

        unopened = flowing - state.opened
        for v in unopened:
            cost: int = min_distances[(state.curr, v)] + 1
            new_elapsed = state.elapsed + cost
            if new_elapsed >= 26:
                continue

            relieved_per_min = 0
            for vopen in state.opened:
                relieved_per_min += valves[vopen].flowrate

            new_opened = state.opened.copy()
            new_opened.add(v)
            new_relieved = state.relieved + (relieved_per_min * cost)
            new_state = State(v, new_opened, new_elapsed, new_relieved)
            state_info = (frozenset(new_opened), new_elapsed, new_relieved)
            if state_info not in seen:
                dq.append(new_state)
                seen.add(state_info)

    for human in max_relieved_states:
        for elephant
    return max_relieved

if __name__ == "__main__":
    print(part_two())
