import heapq
from collections import deque

class PriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.deque = deque()
        self.active = set()
        self.id_counter = 0

    def enqueue(self, item, priority):
        heapq.heappush(self.min_heap, (priority, self.id_counter, item))
        heapq.heappush(self.max_heap, (-priority, self.id_counter, item))
        self.deque.append((self.id_counter, item))
        self.active.add(self.id_counter)
        self.id_counter += 1

    def dequeue(self, mode):
        if not self.active:
            return None

        if mode == "lowest":
            self._clean(self.min_heap, lambda: heapq.heappop(self.min_heap))
            if not self.min_heap:
                return None
            _, i, val = heapq.heappop(self.min_heap)

        elif mode == "highest":
            self._clean(self.max_heap, lambda: heapq.heappop(self.max_heap))
            if not self.max_heap:
                return None
            _, i, val = heapq.heappop(self.max_heap)

        elif mode == "oldest":
            while self.deque and self.deque[0][0] not in self.active:
                self.deque.popleft()
            if not self.deque:
                return None
            i, val = self.deque.popleft()

        elif mode == "newest":
            while self.deque and self.deque[-1][0] not in self.active:
                self.deque.pop()
            if not self.deque:
                return None
            i, val = self.deque.pop()

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
            self._clean(self.min_heap, lambda: heapq.heappop(self.min_heap))
            return self.min_heap[0][2]

        elif mode == "highest":
            self._clean(self.max_heap, lambda: heapq.heappop(self.max_heap))
            return self.max_heap[0][2]

        elif mode == "oldest":
            while self.deque and self.deque[0][0] not in self.active:
                self.deque.popleft()
            return self.deque[0][1]

        elif mode == "newest":
            while self.deque and self.deque[-1][0] not in self.active:
                self.deque.pop()
            return self.deque[-1][1]

        else:
            raise ValueError