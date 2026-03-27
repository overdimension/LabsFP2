from queue import PriorityQueue

pq = PriorityQueue()

pq.enqueue("A", 5)
pq.enqueue("B", 1)
pq.enqueue("C", 10)

print("Stage 1:")
print(pq.data)
print()


print("Stage 3:")
print(pq.peek("highest"))
print(pq.peek("lowest"))
print(pq.peek("newest"))
print(pq.peek("oldest"))
print()


print("Stage 2:")
print(pq.dequeue("highest"))
print(pq.dequeue("lowest"))
print(pq.dequeue("oldest"))
