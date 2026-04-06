import heapq
from collections import deque

class PriorityQueue:
    def __init__(self):
        self.min_h = []
        self.max_h = []
        self.q = deque()
        self.active = set()
        self.i = 0

def enqueue(self, item, priority):
    heapq.heappush(self.min_h, (priority, self.i, item))
    heapq.heappush(self.max_h, (-priority, self.i, item))
    self.q.append((self.i, item))
    self.active.add(self.i)
    self.i += 1

def dequeue(self, mode):
    if not self.active:
        return None

    if mode == "lowest":
        _, i, val = heapq.heappop(self.min_h)

    elif mode == "highest":
        _, i, val = heapq.heappop(self.max_h)

    elif mode == "oldest":
        i, val = self.q.popleft()

    elif mode == "newest":
        i, val = self.q.pop()

    else:
        raise ValueError

    self.active.remove(i)
    return val