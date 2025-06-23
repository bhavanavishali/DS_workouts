from collections import deque

def reverse_queue(q):
    if not q:
        return
    temp=q.popleft()
    reverse_queue(q)
    q.append(temp)

q=deque([1,2,3,4])
print("original queue",q)
reverse_queue(q)
print("reverse Q",q)