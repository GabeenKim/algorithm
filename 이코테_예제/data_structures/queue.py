from collections import deque

queue = deque()

#5, 2, 3, 7 삽입  -> 삭제 -> 삽입 1, 4 -> 삭제 
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft()

queue.append(1)
queue.append(4)

queue.popleft()

print(queue)