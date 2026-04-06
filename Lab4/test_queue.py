from queue import PriorityQueue

pq = PriorityQueue()

pq.enqueue("A", 5)
pq.enqueue("B", 1)
pq.enqueue("C", 10)

print(pq.peek("highest"))  # C
print(pq.peek("lowest"))   # B
print(pq.peek("newest"))   # C
print(pq.peek("oldest"))   # A

print(pq.dequeue("highest")) # C
print(pq.dequeue("lowest"))  # B
print(pq.dequeue("oldest"))  # A
