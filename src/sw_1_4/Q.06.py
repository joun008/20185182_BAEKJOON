#4963번
import sys
sys.setrecursionlimit(10000)
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]

def dfs(x,y):
    if arr[x][y]==1 : 
        arr[x][y]=0
    for k in range(8) :
        nx = x+dx[k]
        ny = y+dy[k]
        if nx<=-1 or nx>=M or ny<=-1 or ny>=N :
            continue
        if arr[nx][ny]==1 :
            arr[nx][ny] = 0
            dfs(nx,ny)


while True :
    check=0
    N,M = map(int,input().split())
    if N==0 and M==0 :
        break
    arr = [list(map(int,input().split())) for _ in range(M)]
    for k in range(N) :
        for j in range(M) :
            if arr[j][k]==1:
                check+=1
                dfs(j,k)
    print(check)
