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

    def dequeue(self, mode):

        active = [x for x in self.data if not x["removed"]]
        if not active:
            return None

        if mode == "highest":
            target = max(active, key=lambda x: x["priority"])

        elif mode == "lowest":
            target = min(active, key=lambda x: x["priority"])

        elif mode == "oldest":
            target = min(active, key=lambda x: x["order"])

        elif mode == "newest":
            target = max(active, key=lambda x: x["order"])

        target["removed"] = True
        return target["item"]