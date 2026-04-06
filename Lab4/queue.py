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
        self._clean(self.min_h, lambda: heapq.heappop(self.min_h))
        _, i, val = heapq.heappop(self.min_h)

    elif mode == "highest":
        self._clean(self.max_h, lambda: heapq.heappop(self.max_h))
        _, i, val = heapq.heappop(self.max_h)

    elif mode == "oldest":
        self._clean(self.q, lambda: self.q.popleft())
        i, val = self.q.popleft()

    elif mode == "newest":
        self._clean(self.q, lambda: self.q.pop())
        i, val = self.q.pop()

    else:
        raise ValueError

    self.active.remove(i)
    return val

def _clean(self, struct, pop_func):
    while struct and struct[0][1] not in self.active:
        pop_func()

def peek(self, mode):
    if not self.active:
        return None

    if mode == "lowest":
        self._clean(self.min_h, lambda: heapq.heappop(self.min_h))
        return self.min_h[0][2]

    elif mode == "highest":
        self._clean(self.max_h, lambda: heapq.heappop(self.max_h))
        return self.max_h[0][2]

    elif mode == "oldest":
        while self.q and self.q[0][0] not in self.active:
            self.q.popleft()
        return self.q[0][1]

    elif mode == "newest":
        while self.q and self.q[-1][0] not in self.active:
            self.q.pop()
        return self.q[-1][1]

    else:
        raise ValueError