from collections import deque
N = int(input())
K = int(input())
apple=[list(map(int,input().split())) for _ in range(K)]
L = int(input())
turn =[list(input().split()) for _ in range(L)]
map = [[0]*(N+1) for _ in range(N+1)]
for t in apple :
    map[t[0]][t[1]]=1
print(map)
print(turn)

x=y=1
time=0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque([[y,x]])
r=0
while True :
    time+=1
    for k in turn :
        if k[0]==time and k[1]=="D":
            r+=1
            if r>=4:
                r-=4
        if k[0]==time and k[1]=="L" :
            r-=1
            if r<0:
                r+=4
    
    ny,nx = queue.popleft()
    print(ny,nx)

