import queue
"""
python has two different modules for queue
queue.Queue is for multi threading
collections.deque is for use of data structure
"""
"""
Default of this module is FIFO
"""
q = queue.Queue()

q.put(4)
q.put(6)
q.put(9)

print(q.qsize())
print(q.get())
print(q.get())
print(q.get())

"""
LIFO queue
"""
q1 = queue.LifoQueue()

q1.put(4)
q1.put(6)
q1.put(9)

print(q1.qsize())
print(q1.get())
print(q1.get())
print(q1.get())

"""
Priority queue
"""

q2 = queue.PriorityQueue()

q2.put(4)
q2.put(9)
q2.put(2)

print(q2.get())
print(q2.get())
print(q2.get())

print(q2.empty())
