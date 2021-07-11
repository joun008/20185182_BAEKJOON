#1697
1)queue에 넣을 때 깊이랑 같이 넣으면 메모리 초과가 발생하므로 visited list를 이용하는 것이 메모리 적으로 좋음

import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())

MAX = 100000
visited =[0] * (MAX+1) //1)

def dfs(N,M) :
    check=0
    queue = deque([N])
    while queue :
        rec = queue.popleft()
        if rec == M:
            print(visited[rec])
            exit()
        for nx in [rec+1,rec-1,rec*2] :
            if 0<=nx<=MAX and visited[nx]==0 :
                visited[nx] = visited[rec]+1 
                queue.append(nx)

dfs(N,M)
