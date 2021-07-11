#1251번
import sys
from collections import deque
N,M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(M)]
visit = [ [-1]*N for _ in range(M)]
dx = [0,1,-1,0]
dy = [-1,0,0,1]

#뿌시는 숫자를 어떻게 셈 하지?
#그 길을 가는데 몇 뻔 뿌신지만 확인 하면 된다
#즉, 0을 우선순위로 가지만 1이 나오면 기존의 뿌신 벽 수 유지
#1이 나오면 뿌신 벽+1

def bfs() :
    queue = deque([[0,0]])
    visit[0][0] = 0
    while queue :        
        T = queue.popleft()
        y = T[0]
        x = T[1]
        if y==M-1 and x==N-1 :
            print(visit[y][x])
            exit()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<=-1 or nx>=N  or ny<=-1 or ny>=M :
                continue

            if maze[ny][nx]==0 and visit[ny][nx]==-1 :
                visit[ny][nx] = visit[y][x]
                queue.appendleft([ny,nx])

            if maze[ny][nx]==1 and visit[ny][nx]==-1 :
                visit[ny][nx] = visit[y][x]+1
                queue.append([ny,nx])

bfs()
