import heapq
from collections import deque

class PriorityQueue:
    def __init__(self):
        self.min_h = []
        self.max_h = []
        self.q = deque()
        self.active = set()
        self.i = 0