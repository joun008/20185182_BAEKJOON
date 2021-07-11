#13549번
핵심은 2배로 갈때는 시간이 똑같으니까 우선순위가 존재함
import sys
input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
MAX=100000
visit = [-1]*(MAX+1)
def bfs(N,M) :
    queue = deque([N])
    visit[N]=0
    while queue :
        t = queue.popleft()
        if t==M :
            print(visit[t])
            exit()
        for k in [t-1,t+1,2*t] :
            if 0<=k<=MAX and visit[k]==-1:
                if k==2*t :
                    queue.appendleft(k)
                    visit[k] = visit[t]
                else :
                    queue.append(k)
                    visit[k]=visit[t]+1
        
bfs(N,M)
