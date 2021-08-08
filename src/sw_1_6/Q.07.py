N = int(input())

dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

arr = [[0]*N for _ in range(N)]
visited =[[False]*N for _ in range(N)]

count=0

def direction(y,x,r) :
    visited[y][x]=True
    arr[y][x]=1
    if x+dx[r]>=N or x+dx[r]<0 or y+dy[r]>=N or y+dy[r]<0 :
        return
    
    direction(y+dy[r],x+dx[r],r)
    visited[y][x]=False

for k in range(N) :
    for j in range(N) :
        if arr[k][j]==0 and visited:
            count+=1
            for d in range(8) :
                direction(k,j,d)
            
            
print(arr,count)