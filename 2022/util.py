class Heap:
    def __init__(self, items) -> None:
        self.items = items
        self._heapify()

    # bottom up heapify
    def _heapify(self):
        curr_index = len(self.items) - 1
        while curr_index > 0:
            child_index = curr_index
            parent_index = ((child_index + 1) // 2)  - 1
            while parent_index > -1 and self.items[parent_index] > self.items[child_index]:
                self.items[child_index], self.items[parent_index] = self.items[parent_index], self.items[child_index]
                child_index = parent_index
                parent_index = ((child_index + 1) // 2)  - 1
            curr_index -= 1

    def push(self, item):
        self.items.append(item)
        self._heapify()

    def pop(self):
        item = self.items.pop(0)
        self._heapify()
        return item


'''Similiar to CS50 AI implementation of Frontiers for BFS or DFS Algorithm'''
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
