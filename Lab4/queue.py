class PriorityQueue:
    def __init__(self):
        self.data = []
        self.counter = 0

    def enqueue(self, item, priority):
        self.data.append({
            "item": item,
            "priority": priority,
            "order": self.counter,
            "removed": False
        })
        self.counter += 1