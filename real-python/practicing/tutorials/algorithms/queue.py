from collections import deque

# * deque is used for adding and rremoving element from both ends of the collection

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
x = queue.popleft()
print(x)
print(queue)
