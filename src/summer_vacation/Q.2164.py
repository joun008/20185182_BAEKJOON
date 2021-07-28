from collections import deque
N = int(input())
queue = deque([k for k in range(1,N+1)])
for k in range(N-1) :
    queue.popleft()
    ma = queue.popleft()
    queue.append(ma)

print(queue.popleft())