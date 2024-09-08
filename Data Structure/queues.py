from collections import deque

queue = deque()

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue elements
first_in = queue.popleft()
print(first_in)  # Output: 1

# Peek at the first element
print(queue[0])  # Output: 2
