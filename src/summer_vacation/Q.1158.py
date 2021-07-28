#queue를 이용하지 않는 풀이
'''
N,K = map(int,input().split())
visited = [0]*(N+1)
count=0
num = []
for t in range(N) :
    count_= 0
    for k in range(N*N):
        count+=1
        if count>N :
            count-=N
        if visited[count]==0:
            count_+=1
        if count_==K:
            break

    visited[count]=1    
    num.append(count)

print("<", end = '')
print(*num, sep = ', ', end = '')
print(">")
'''
#queue를 이용한 풀이
from collections import deque
N,K = map(int,input().split())
queue = deque([i for i in range(1,N+1)])
num =[]
for t in range(N) :
    for j in range(K-1):
        ma =queue.popleft()
        queue.append(ma)
    num.append(queue.popleft())
print("<", end = '')
print(*num, sep = ', ', end = '')
print(">")
    