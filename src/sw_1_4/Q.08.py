#7576번 - 토마토 문제
import sys
input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs() :
    global data
    queue = deque(data)
    while queue :
        T = queue.popleft()
        y = T[0]
        x = T[1]

        for k in range(4) :
            nx = x +dx[k]
            ny = y +dy[k]
            if nx<=-1 or nx>=N or ny<=-1 or ny>=M :
                continue
            if arr[ny][nx] == 0 :
                arr[ny][nx] = arr[y][x]+1
                queue.append((ny,nx))
data=[]
for k in range(N) :
    for j in range(M) :
        if arr[j][k] == 1 :
            data.append((j,k))
bfs()
Max=0
check = True
for k in range(N) :
    for j in range(M) :
        Max = max(Max,arr[j][k])
        if arr[j][k] == 0 :
            check = False
            print(-1)
            exit()
            
if check :
    print(Max-1)
